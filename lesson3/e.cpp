#include <iostream>
#include <limits>
#include <string>
#include <map>
#include <tuple>
#include <set>
#include <fstream>
#include <vector>


class Point
{
public:
    Point()
    {}

    bool visited = false;
    double dist = std::numeric_limits<double>::max();
    std::string from_point = "";
};

std::map<std::string, Point> dijkstraSearch(std::map<std::string, std::map<std::string, double>> graph, std::string point_from)
{
    std::map<std::string, Point > points_data;
    for (auto &point : graph)
    {
        points_data[point.first] = Point();

        if (point.first == point_from)
        {
            points_data[point.first].dist = 0;
        }
    }

    bool all_pts_checked = false;
    std::string curr_point;

    int curr_dist;

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

            if (graph.count(curr_point))
            {
                for (auto &neighbor : graph[curr_point])
                {
                    curr_dist = points_data[curr_point].dist + graph[curr_point][neighbor.first];

                    if (!points_data.count(neighbor.first))
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

std::map<std::string, std::map<std::string, double>>  find_time_to_neighbors(std::string origin_city, std::string from_city, double prev_time, int speed, std::map<std::string, std::map<std::string, double>> roads, std::map<std::string, std::map<std::string, double>> times)
{
    if (from_city != "1")
    {
        for (auto &to_city : roads[from_city])
        {
            if (to_city.first != from_city && to_city.first != origin_city)
            {

                if (!times.count(to_city.first))
                {
                    std::map<std::string, double> new_clean_map;
                    times[to_city.first] = new_clean_map;
                }

                if (!times[to_city.first].count(origin_city))
                {
                    times[to_city.first][origin_city] = prev_time + roads[to_city.first][from_city] / speed;

                    times = find_time_to_neighbors(origin_city, to_city.first, times[to_city.first][origin_city], speed, roads, times);
                }
            }
        }
    }
    return times;
}


std::map<std::string, std::map<std::string, double>> time_searcher(std::map<std::string, std::map<std::string, double>> roads,  std::map<std::string, std::tuple<int, int>> city_info, std::map<std::string, std::map<std::string, double>> times, std::set<std::string> visited_cities)
{
    int prep_time = 0, speed = 0;
    double prev_time = 0;
    for (auto &from_city : roads)
    {
        if (visited_cities.find(from_city.first) == visited_cities.end() && from_city.first != "1")
        {
            
            prep_time = std::get<0>(city_info[from_city.first]);
            speed = std::get<1>(city_info[from_city.first]);

            prev_time = 0;

            for (auto &to_city : roads[from_city.first])
            {
                if ( !times.count(to_city.first) )
                {
                    std::map<std::string, double> new_clean_map;
                    times[to_city.first] = new_clean_map;
                }

                if ( !times[to_city.first].count(from_city.first) )
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


int main()
{

    std::ifstream f;
    f.open("input.txt");
    int N;
    f >> N;

    std::map<std::string, std::map<std::string, double>> roads;
    std::map<std::string, std::tuple<int, int>> city_info;

    int prep_time, speed;

    for ( int city_id = 1; city_id < N+1; city_id++)
    {
        f >> prep_time >> speed;

        std::tuple<int, int> sample_tuple(prep_time, speed);
        city_info[std::to_string(city_id)] = sample_tuple;

    }

    std::string from_id, to_id, dist;
    int dist_int;

    for ( int i = 1; i <= N-1; i++)
    {
        f >> from_id >> to_id >> dist;

        dist_int = std::stoi(dist);

        if (! roads.count(from_id))
        {
            std::map<std::string, double> clean_roads_map;
            roads[from_id] = clean_roads_map;
        }

        if (! roads[from_id].count(to_id))
        {
            roads[from_id][to_id] = 0;
        }

        if (! roads.count(to_id))
        {
            std::map<std::string, double> clean_roads_map;
            roads[to_id] = clean_roads_map;
        }

        if (! roads[to_id].count(from_id))
        {
            roads[to_id][from_id] = 0;
        }

        roads[from_id][to_id] = dist_int;
        roads[to_id][from_id] = dist_int;
    }



    std::map<std::string, std::map<std::string, double>> times;
    std::set<std::string> visited_cities;

    std::map<std::string, std::map<std::string, double>> res = time_searcher(roads, city_info, times, visited_cities);

    std::string max_pt;
    double max_d = 0;
    std::map<std::string, Point> points_data = dijkstraSearch(res, "1");

    for (auto &point : points_data)
    {
        if (max_d < point.second.dist)
        {
            max_d = point.second.dist;
            max_pt = point.first;
        }
    }

    std::vector<std::string> restored_path;
    restored_path.push_back(max_pt);

    std::string curr_point = points_data[max_pt].from_point;

    while (curr_point != "")
    { // what the fuck
        restored_path.push_back(curr_point);
        curr_point = points_data[curr_point].from_point;
    }

    std::cout << max_d << std::endl;

    for (int i = 0 ; i < restored_path.size() - 1; i++)
    {
        std::cout << restored_path[i] << " ";
    }
    std::cout << restored_path.back();
}