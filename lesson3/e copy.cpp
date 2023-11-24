#include <iostream>
#include <limits>
#include <string>
#include <unordered_map> 
#include <tuple>
#include <set>
#include <fstream>
#include <vector>
#include <iomanip>
// #include <numbers>

class Point
{
public:
    Point()
    {}

    bool visited = false;
    double dist = std::numeric_limits<double>::max();
    int from_point = -1;
};

std::unordered_map<int, Point> dijkstraSearch(std::unordered_map<int, std::unordered_map<int, double>>& graph, int& point_from)
{
    std::unordered_map<int, Point > points_data;
    for (auto &point : graph)
    {
        points_data[point.first] = Point();

        if (point.first == point_from)
        {
            points_data[point.first].dist = 0;
        }
    }

    bool all_pts_checked = false;
    int curr_point;

    double curr_dist;

    while (!all_pts_checked)
    {
        all_pts_checked = true;
        for (auto &point : points_data)
        {
            if (!point.second.visited)
            {
                curr_point = point.first;
                all_pts_checked = false;
                break;
            }
        }

        if (!all_pts_checked)
        {
            for (auto &point : points_data)
            {// wtf is here
                if (point.second.dist < points_data[curr_point].dist && !point.second.visited)
                {
                    curr_point = point.first;
                }
            }

            if (graph.find(curr_point) != graph.end())
            {
                for (auto &neighbor : graph[curr_point])
                {
                    curr_dist = points_data[curr_point].dist + graph[curr_point][neighbor.first];

                    if (points_data.find(neighbor.first) == points_data.end())
                    {
                        points_data[neighbor.first] = Point();
                    }

                    if (curr_dist < points_data[neighbor.first].dist)
                    {
                        points_data[neighbor.first].dist = curr_dist;
                        points_data[neighbor.first].from_point = curr_point;
                    }
                }
            }

            points_data[curr_point].visited = true;
        }
    }

    return points_data;
}

std::unordered_map<int, std::unordered_map<int, double>>  find_time_to_neighbors(int origin_city, int from_city, double& prev_time, int& speed, std::unordered_map<int, std::unordered_map<int, double>>& roads, std::unordered_map<int, std::unordered_map<int, double>>& times)
{
    if (from_city != 1)
    {
        for (auto &to_city : roads[from_city])
        {
            if (to_city.first != from_city && to_city.first != origin_city)
            {

                if (times.find(to_city.first) == times.end())
                {
                    std::unordered_map<int, double> new_clean_unordered_map;
                    times[to_city.first] = new_clean_unordered_map;
                }

                if (times[to_city.first].find(origin_city) == times[to_city.first].end())
                {
                    times[to_city.first][origin_city] = prev_time + roads[to_city.first][from_city] / speed;

                    times = find_time_to_neighbors(origin_city, to_city.first, times[to_city.first][origin_city], speed, roads, times);
                }
            }
        }
    }
    return times;
}


std::unordered_map<int, std::unordered_map<int, double>> time_searcher(std::unordered_map<int, std::unordered_map<int, double>>& roads,  std::unordered_map<int, std::tuple<int, int>>& city_info, std::unordered_map<int, std::unordered_map<int, double>>& times, std::set<int>& visited_cities)
{
    int prep_time = 0, speed = 0;
    double prev_time = 0;
    for (auto &from_city : roads)
    {
        if (visited_cities.find(from_city.first) == visited_cities.end() && from_city.first != 1)
        {
            
            prep_time = std::get<0>(city_info[from_city.first]);
            speed = std::get<1>(city_info[from_city.first]);

            prev_time = 0;

            for (auto &to_city : roads[from_city.first])
            {
                if ( times.find(to_city.first) == times.end() )
                {
                    std::unordered_map<int, double> new_clean_unordered_map;
                    times[to_city.first] = new_clean_unordered_map;
                }

                if ( times[to_city.first].find(from_city.first) == times[to_city.first].end() )
                {
                    times[to_city.first][from_city.first] = prep_time + roads[to_city.first][from_city.first] / speed;

                    prev_time = times[to_city.first][from_city.first];

                    times = find_time_to_neighbors(from_city.first, to_city.first, prev_time, speed, roads, times);

                }
            }

            visited_cities.insert(from_city.first);
        }
    }

    return times;
}

int NumDigits(double& x)  
{   
    return (x < 10 ? 1 :   
        (x < 100 ? 2 :   
        (x < 1000 ? 3 :   
        (x < 10000 ? 4 :   
        (x < 100000 ? 5 :   
        (x < 1000000 ? 6 :   
        (x < 10000000 ? 7 :  
        (x < 100000000 ? 8 :  
        (x < 1000000000 ? 9 :  
        10)))))))));  
}  

int main()
{
    std::ifstream f;
    f.open("input.txt");
    int N;
    f >> N;

    std::unordered_map<int, std::unordered_map<int, double>> roads;
    std::unordered_map<int, std::tuple<int, int>> city_info;

    int prep_time, speed;

    for ( int city_id = 1; city_id < N+1; city_id++)
    {
        f >> prep_time >> speed;

        std::tuple<int, int> sample_tuple(prep_time, speed);
        city_info[city_id] = sample_tuple;

    }

    int from_id, to_id, dist;
    int dist_int;

    for ( int i = 1; i <= N-1; i++)
    {
        f >> from_id >> to_id >> dist;

        dist_int = dist;

        if ( roads.find(from_id) == roads.end())
        {
            std::unordered_map<int, double> clean_roads_unordered_map;
            roads[from_id] = clean_roads_unordered_map;
        }

        if ( roads[from_id].find(to_id) == roads[from_id].end())
        {
            roads[from_id][to_id] = 0;
        }

        if (roads.find(to_id) == roads.end())
        {
            std::unordered_map<int, double> clean_roads_unordered_map;
            roads[to_id] = clean_roads_unordered_map;
        }

        if (roads[to_id].find(from_id) == roads[to_id].end())
        {
            roads[to_id][from_id] = 0;
        }

        roads[from_id][to_id] = dist_int;
        roads[to_id][from_id] = dist_int;
    }



    std::unordered_map<int, std::unordered_map<int, double>> times;
    std::set<int> visited_cities;

    std::unordered_map<int, std::unordered_map<int, double>> res = time_searcher(roads, city_info, times, visited_cities);
    // std::cout << "don this part" << std::endl;

    int max_pt;
    double max_d = 0;
    int strt = 1;
    std::unordered_map<int, Point> points_data = dijkstraSearch(res, strt);

    for (auto &point : points_data)
    {
        if (max_d < point.second.dist)
        {
            max_d = point.second.dist;
            max_pt = point.first;
        }
    }

    std::vector<int> restored_path;
    restored_path.push_back(max_pt);

    int curr_point = points_data[max_pt].from_point;

    while (curr_point != -1)
    {
        restored_path.push_back(curr_point);
        curr_point = points_data[curr_point].from_point;
    }

    int n = NumDigits(max_d);

    std::cout << std::setprecision(n+4) << max_d  << std::endl;
    // std::cout << max_d  << std::endl;

    for (int i = 0 ; i < restored_path.size() - 1; i++)
    {
        std::cout << restored_path[i] << " ";
    }
    std::cout << restored_path.back();
}