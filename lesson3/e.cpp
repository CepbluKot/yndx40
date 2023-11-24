#include <iostream>
#include <limits>
#include <string>
#include <unordered_map> 
#include <tuple>
#include <set>
#include <fstream>
#include <vector>
#include <iomanip>


class Point
{
public:
    Point()
    {}

    bool visited = false;
    double dist =  std::numeric_limits<double>::max();
    unsigned short from_point =  0;
};

void dijkstraSearch(std::unordered_map<unsigned short, std::unordered_map<unsigned short, double>>& graph, unsigned short& point_from, std::unordered_map<unsigned short, Point*>& points_data)
{
    for (auto &point : graph)
    {
        points_data[point.first] = new Point();

        if (point.first == point_from)
        {
            points_data[point.first]->dist = 0;
        }
    }

    bool all_pts_checked =  false;
    unsigned short curr_point ;

    double curr_dist ;

    while (!all_pts_checked)
    {
        all_pts_checked = true;
        for (auto &point : points_data)
        {
            if (!point.second->visited)
            {
                curr_point = point.first;
                all_pts_checked = false;
                break;
            }
        }

        if (!all_pts_checked)
        {
            for (auto &point : points_data)
            {
                if (point.second->dist < points_data[curr_point]->dist && !point.second->visited)
                {
                    curr_point = point.first;
                }
            }

            if (graph.find(curr_point) != graph.end())
            {
                for (auto &neighbor : graph[curr_point])
                {
                    curr_dist = points_data[curr_point]->dist + graph[curr_point][neighbor.first];

                    if (points_data.find(neighbor.first) == points_data.end())
                    {
                        points_data[neighbor.first] = new Point();
                    }

                    if (curr_dist < points_data[neighbor.first]->dist)
                    {
                        points_data[neighbor.first]->dist = curr_dist;
                        points_data[neighbor.first]->from_point = curr_point;
                    }
                }
            }

            points_data[curr_point]->visited = true;
        }
    }

    // return points_data;
}

void  find_time_to_neighbors(unsigned short origin_city, unsigned short from_city, double& prev_time, unsigned short& speed, std::unordered_map<unsigned short, std::unordered_map<unsigned short, unsigned short>>& roads, std::unordered_map<unsigned short, std::unordered_map<unsigned short, double>>& times)
{
    if (from_city != 1)
    {
        for (auto &to_city : roads[from_city])
        {
            if (to_city.first != from_city && to_city.first != origin_city)
            {

                if (times.find(to_city.first) == times.end())
                {
                    std::unordered_map<unsigned short, double> new_clean_unordered_map;
                    times[to_city.first] = new_clean_unordered_map;
                }

                if (times[to_city.first].find(origin_city) == times[to_city.first].end())
                {
                    times[to_city.first][origin_city] = prev_time + (double)roads[to_city.first][from_city] / (double)speed;

                    find_time_to_neighbors(origin_city, to_city.first, times[to_city.first][origin_city], speed, roads, times);
                }
            }
        }
    }
    // return times;
}


void time_searcher(std::unordered_map<unsigned short, std::unordered_map<unsigned short, unsigned short>>& roads,  std::unordered_map<unsigned short, std::tuple<unsigned short, unsigned short>>& city_info, std::unordered_map<unsigned short, std::unordered_map<unsigned short, double>>& times, std::set<unsigned short>& visited_cities)
{
    unsigned short prep_time = 0, speed = 0;
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
                    std::unordered_map<unsigned short, double> new_clean_unordered_map;
                    times[to_city.first] = new_clean_unordered_map;
                }

                if ( times[to_city.first].find(from_city.first) == times[to_city.first].end() )
                {
                    times[to_city.first][from_city.first] = prep_time + (double)roads[to_city.first][from_city.first] / (double)speed;

                    prev_time = times[to_city.first][from_city.first];

                    find_time_to_neighbors(from_city.first, to_city.first, prev_time, speed, roads, times);

                }
            }

            visited_cities.insert(from_city.first);
        }
    }

    // return times;
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
    unsigned short N;
    f >> N;

    std::unordered_map<unsigned short, std::unordered_map<unsigned short, unsigned short>> roads;
    std::unordered_map<unsigned short, std::tuple<unsigned short, unsigned short>> city_info;

    unsigned short prep_time, speed;

    for ( unsigned short city_id = 1; city_id < N+1; city_id++)
    {
        f >> prep_time >> speed;

        std::tuple<unsigned short, unsigned short> sample_tuple(prep_time, speed);
        city_info[city_id] = sample_tuple;

    }

    unsigned short from_id, to_id, dist;
    unsigned short dist_int;

    for ( unsigned short i = 1; i <= N-1; i++)
    {
        f >> from_id >> to_id >> dist;

        dist_int = dist;

        if ( roads.find(from_id) == roads.end())
        {
            std::unordered_map<unsigned short, unsigned short> clean_roads_unordered_map;
            roads[from_id] = clean_roads_unordered_map;
        }

        if ( roads[from_id].find(to_id) == roads[from_id].end())
        {
            roads[from_id][to_id] = 0;
        }

        if (roads.find(to_id) == roads.end())
        {
            std::unordered_map<unsigned short, unsigned short> clean_roads_unordered_map;
            roads[to_id] = clean_roads_unordered_map;
        }

        if (roads[to_id].find(from_id) == roads[to_id].end())
        {
            roads[to_id][from_id] = 0;
        }

        roads[from_id][to_id] = dist_int;
        roads[to_id][from_id] = dist_int;
    }



    std::unordered_map<unsigned short, std::unordered_map<unsigned short, double>> times;
    std::set<unsigned short> visited_cities;

    time_searcher(roads, city_info, times, visited_cities);
    // std::unordered_map<int, std::unordered_map<int, float>> res= times;
    // std::cout << "don this part" << std::endl;

    unsigned short max_pt;
    double max_d = 0;
    unsigned short strt = 1;
    std::unordered_map<unsigned short, Point*> points_data;



    dijkstraSearch(times, strt, points_data);

    for (auto &point : points_data)
    {
        if (max_d < point.second->dist)
        {
            max_d = point.second->dist;
            max_pt = point.first;
        }
    }

    std::vector<unsigned short> restored_path;
    restored_path.push_back(max_pt);

    unsigned short curr_point = points_data[max_pt]->from_point;

    while (curr_point != 0)
    {
        restored_path.push_back(curr_point);
        curr_point = points_data[curr_point]->from_point;
    }

    unsigned short n = NumDigits(max_d);

    std::cout << std::setprecision(n+4) << max_d  << std::endl;
    // std::cout << max_d  << std::endl;

    for (unsigned short i = 0 ; i < restored_path.size() - 1; i++)
    {
        std::cout << restored_path[i] << " ";
    }
    std::cout << restored_path.back();
}