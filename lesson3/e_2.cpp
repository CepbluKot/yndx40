#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <limits>

class Point {
public:
    bool visited = false;
    double dist = std::numeric_limits<double>::infinity();
    std::string from_point = "";
};

std::unordered_map<std::string, Point> deikstraSearch( std::unordered_map<std::string, std::unordered_map<std::string, double>>& graph,  std::string& point_from) {
    std::unordered_map<std::string, Point> points_data;

    for ( auto& point : graph) {
        Point new_point;
        if (point.first == point_from) {
            new_point.dist = 0;
        }
        points_data[point.first] = new_point;
    }

    bool all_pts_checked = false;
    while (!all_pts_checked) {
        all_pts_checked = true;

        std::string curr_point;
        for ( auto& point : points_data) {
            if (!point.second.visited) {
                curr_point = point.first;
                all_pts_checked = false;
                break;
            }
        }

        if (!all_pts_checked) {
            for ( auto& point : points_data) {
                if (points_data[point.first].dist < points_data[curr_point].dist && !points_data[point.first].visited) {
                    curr_point = point.first;
                }
            }

            for ( auto& neighbor : graph.at(curr_point)) {
                double curr_dist = points_data[curr_point].dist + graph.at(curr_point).at(neighbor);

                if (curr_dist < points_data[neighbor].dist) {
                    points_data[neighbor].dist = curr_dist;
                    points_data[neighbor].from_point = curr_point;
                }
            }

            points_data[curr_point].visited = true;
        }
    }

    return points_data;
}

void findTimeToNeighbors( std::string& origin_city,  std::string& from_city, double prev_time, int speed,  std::unordered_map<std::string, std::unordered_map<std::string, double>>& roads, std::unordered_map<std::string, std::unordered_map<std::string, double>>& times) {
    if (from_city != "1") {
        for ( auto& to_city : roads.at(from_city)) {
            if (to_city != from_city && to_city != origin_city) {
                if (times.find(origin_city) == times.end()) {
                    times[origin_city] = {};
                }
                if (times[origin_city].find(to_city) == times[origin_city].end()) {
                    times[origin_city][to_city] = prev_time + roads.at(from_city).at(to_city) / speed;

                    findTimeToNeighbors(origin_city, to_city, times[origin_city][to_city], speed, roads, times);
                }
            }
        }
    }
}

std::unordered_map<std::string, std::unordered_map<std::string, double>> timeSearcher( std::unordered_map<std::string, std::unordered_map<std::string, double>>& roads,  std::unordered_map<std::string, std::pair<int, int>>& city_info) {
    std::unordered_map<std::string, std::unordered_map<std::string, double>> times;

    std::unordered_set<std::string> visited_cities;

    for ( auto& from_city : roads) {
        if (visited_cities.find(from_city.first) == visited_cities.end() && from_city.first != "1") {
            int prep_time = city_info.at(from_city.first).first;
            int speed = city_info.at(from_city.first).second;
            double prev_time = 0;

            for ( auto& to_city : from_city.second) {
                if (times.find(from_city.first) == times.end()) {
                    times[from_city.first] = {};
                }
                if (times[from_city.first].find(to_city.first) == times[from_city.first].end()) {
                    times[from_city.first][to_city.first] = prep_time + from_city.second.at(to_city.first) / speed;

                    prev_time = times[from_city.first][to_city.first];

                    findTimeToNeighbors(from_city.first, to_city.first, prev_time, speed, roads, times);
                }
            }

            visited_cities.insert(from_city.first);
        }
    }

    return times;
}

int main() {
    std::ifstream file("input.txt");
    int N;
    file >> N;

    std::unordered_map<std::string, std::unordered_map<std::string, double>> roads;
    std::unordered_map<std::string, std::pair<int, int>> city_info;

    for (int city_id = 1; city_id <= N; ++city_id) {
        int prep_time, speed;
        file >> prep_time >> speed;
        city_info[std::to_string(city_id)] = std::make_pair(prep_time, speed);
    }

    for (int i = 0; i < N - 1; ++i) {
        int from_id, to_id, dist;
        file >> from_id >> to_id >> dist;

        if (roads.find(std::to_string(from_id)) == roads.end()) {
            roads[std::to_string(from_id)] = {};
        }

        if (roads[std::to_string(from_id)].find(std::to_string(to_id)) == roads[std::to_string(from_id)].end()) {
            roads[std::to_string(from_id)][std::to_string(to_id)] = 0;
        }

        if (roads.find(std::to_string(to_id)) == roads.end()) {
            roads[std::to_string(to_id)] = {};
        }

        if (roads[std::to_string(to_id)].find(std::to_string(from_id)) == roads[std::to_string(to_id)].end()) {
            roads[std::to_string(to_id)][std::to_string(from_id)] = 0;
        }

        roads[std::to_string(from_id)][std::to_string(to_id)] = dist;
        roads[std::to_string(to_id)][std::to_string(from_id)] = dist;
    }

    auto res = timeSearcher(roads, city_info);
    std::unordered_map<std::string, std::unordered_map<std::string, double>> new_res;

    std::vector<std::string> from_city_keys;
    for ( auto& entry : res) {
        from_city_keys.push_back(entry.first);
    }

    while (!from_city_keys.empty()) {
        std::string from_city = from_city_keys.back();
        from_city_keys.pop_back();
        std::vector<std::string> to_city_keys;

        for ( auto& entry : res[from_city]) {
            to_city_keys.push_back(entry.first);
        }

        while (!to_city_keys.empty()) {
            std::string to_city = to_city_keys.back();
            to_city_keys.pop_back();

            if (new_res.find(to_city) == new_res.end()) {
                new_res[to_city] = {};
            }

            new_res[to_city][from_city] = res[from_city][to_city];
            res[from_city].erase(to_city);
        }
    }

    for (int city_id = 1; city_id <= N; ++city_id) {
        std::string city_str = std::to_string(city_id);
        if (new_res.find(city_str) == new_res.end()) {
            new_res[city_str] = {};
        }
    }

    std::string max_pt;
    double max_d = 0;

    auto points_data = deikstraSearch(new_res, "1");
    for ( auto& point : points_data) {
        if (max_d < point.second.dist) {
            max_d = point.second.dist;
            max_pt = point.first;
        }
    }

    std::vector<std::string> restored_path;
    restored_path.push_back(max_pt);
    std::string curr_point = points_data[max_pt].from_point;
    while (!curr_point.empty()) {
        restored_path.push_back(curr_point);
        curr_point = points_data[curr_point].from_point;
    }

    std::cout << max_d << std::endl;
    for ( auto& city : restored_path) {
        std::cout << city << " ";
    }

    return 0;
}
