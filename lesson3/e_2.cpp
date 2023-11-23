#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <limits>

class Point {
public:
    bool visited;
    double dist;
    std::string from_point;

    Point() : visited(false), dist(std::numeric_limits<double>::infinity()) {}
};

void find_time_to_neighbors(
    const std::string& origin_city,
    const std::string& from_city,
    double prev_time,
    int speed,
    const std::unordered_map<std::string, std::unordered_map<std::string, int>>& roads,
    std::unordered_map<std::pair<std::string, std::string>, double>& times
) {
    if (from_city != "1") {
        for (const auto& road : roads.at(from_city)) {
            const std::string& to_city = road.first;

            if (to_city != from_city && to_city != origin_city) {
                if (times.find({origin_city, to_city}) == times.end()) {
                    times[{origin_city, to_city}] = prev_time + static_cast<double>(road.second) / speed;

                    find_time_to_neighbors(origin_city, to_city, times[{origin_city, to_city}], speed, roads, times);
                }
            }
        }
    }
}

std::unordered_map<std::pair<std::string, std::string>, double> time_searcher(
    const std::unordered_map<std::string, std::unordered_map<std::string, int>>& roads,
    const std::unordered_map<std::string, std::pair<int, int>>& city_info
) {
    std::unordered_map<std::pair<std::string, std::string>, double> times;

    for (const auto& entry : roads) {
        const std::string& from_city = entry.first;

        if (from_city != "1") {
            double prev_time = 0;
            int speed = city_info.at(from_city).second;

            for (const auto& road : entry.second) {
                const std::string& to_city = road.first;

                if (times.find({from_city, to_city}) == times.end()) {
                    times[{from_city, to_city}] = city_info.at(from_city).first + static_cast<double>(road.second) / speed;

                    prev_time = times[{from_city, to_city}];

                    find_time_to_neighbors(from_city, to_city, prev_time, speed, roads, times);
                }
            }
        }
    }

    return times;
}

std::unordered_map<std::string, Point> dijkstraSearchFast(
    const std::unordered_map<std::string, std::unordered_map<std::string, double>>& graph,
    const std::string& point_from
) {
    std::unordered_map<std::string, Point> points_data;
    std::priority_queue<std::pair<double, std::string>, std::vector<std::pair<double, std::string>>, std::greater<>> pts_heap;

    for (const auto& entry : graph) {
        Point new_point;

        if (entry.first == point_from) {
            if (entry.second.find(point_from) == entry.second.end()) {
                new_point.dist = 0;
            } else {
                new_point.dist = entry.second.at(point_from);
            }
        }

        points_data[entry.first] = new_point;
        pts_heap.push({new_point.dist, entry.first});
    }

    bool all_pts_checked = false;
    while (!all_pts_checked) {
        all_pts_checked = true;

        if (!pts_heap.empty()) {
            all_pts_checked = false;

            const std::string& curr_point = pts_heap.top().second;
            pts_heap.pop();

            if (!points_data[curr_point].visited) {
                for (const auto& neighbor : graph.at(curr_point)) {
                    double curr_dist = points_data[curr_point].dist + neighbor.second;

                    if (curr_dist < points_data[neighbor.first].dist) {
                        points_data[neighbor.first].dist = curr_dist;
                        points_data[neighbor.first].from_point = curr_point;
                        pts_heap.push({points_data[neighbor.first].dist, neighbor.first});
                    }
                }

                points_data[curr_point].visited = true;
            }
        } else {
            all_pts_checked = true;
        }
    }

    return points_data;
}

int main() {
    // Read input from file or standard input

    int N;
    std::cin >> N;

    std::unordered_map<std::string, std::unordered_map<std::string, int>> roads;
    std::unordered_map<std::string, std::pair<int, int>> city_info;

    for (int city_id = 1; city_id <= N; ++city_id) {
        int prep_time, speed;
        std::cin >> prep_time >> speed;

        city_info[std::to_string(city_id)] = {prep_time, speed};
    }

    for (int i = 0; i < N - 1; ++i) {
        std::string from_id, to_id;
        int dist;

        std::cin >> from_id >> to_id >> dist;

        roads[from_id][to_id] = dist;
        roads[to_id][from_id] = dist;
    }

    // Perform time search and build the graph
    auto res = time_searcher(roads, city_info);

    std::unordered_map<std::string, std::unordered_map<std::string, double>> graph = {{"1", {}}};
    for (const auto& road : res) {
        const std::string& from_city = road.first.first;
        const std::string& to_city = road.first.second;

        if (graph.find(from_city) == graph.end()) {
            graph[from_city] = {};
        }

        graph[from_city][to_city] = road.second;
    }

    // Find the maximum distance and the corresponding path
    std::string max_pt;
    double max_d = 0;
    std::unordered_map<std::string, Point> max_pts_data;

    for (int city_id = 2; city_id <= N; ++city_id) {
        std::unordered_map<std::string, Point> points_data = dijkstraSearchFast(graph, std::to_string(city_id));

        if (max_d < points_data["1"].dist) {
            max_pts_data = points_data;
            max_d = points_data["1"].dist;
            max_pt = std::to_string(city_id);
        }
    }

    // Restore and print the path
    std::vector<std::string> restored_path = {"1"};
    std::string curr_point = max_pts_data["1"].from_point;

    while (!curr_point.empty()) {
        restored_path.push_back(curr_point);
        curr_point = max_pts_data[curr_point].from_point;
    }

    std::cout << max_d << std::endl;
    for (auto it = restored_path.rbegin(); it != restored_path.rend(); ++it) {
        std::cout << *it << " ";
    }

    return 0;
}
