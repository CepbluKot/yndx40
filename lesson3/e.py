import math
import heapq


class CityTimes:
    fastest_time_to_get_here = math.inf
    fastest_from = None


class Point:
    visited = False
    dist = math.inf
    from_point = None


def deikstraSearchFast(
    graph: dict,
    point_from: str
):
    points_data = {}
    max_dist = 0
    point_w_max_dist = None
    
    pts_heap = []
    heapq.heapify(pts_heap)


    for point in graph:
        new_point = Point()
        if point == point_from:
            if not point_from in graph[point]:
                new_point.dist = 0
            else:
                new_point.dist = graph[point][point_from]
        
        points_data[point] = new_point
        heapq.heappush(pts_heap, (new_point.dist, point))


    all_pts_checked = False
    while not all_pts_checked:
        all_pts_checked = True
        if pts_heap:
            all_pts_checked = False
            curr_point = heapq.heappop(pts_heap)[1]
            if not points_data[curr_point].visited:
                

                for neighbor in graph[curr_point]:
                    curr_dist = points_data[curr_point].dist + graph[curr_point][neighbor]

                    if curr_dist < points_data[neighbor].dist:
                        if curr_dist > max_dist:
                            max_dist = curr_dist
                            point_w_max_dist = neighbor
                        
                        points_data[neighbor].dist = curr_dist
                        points_data[neighbor].from_point = curr_point
                        heapq.heappush(pts_heap, (points_data[neighbor].dist, neighbor))

                
                points_data[curr_point].visited = True
            
        else:
            all_pts_checked = True

    return points_data, max_dist, point_w_max_dist



def time_searcher(roads: dict, city_info: dict, path: dict={}, times: dict={}, end_city:int = '1'):
    # times: key = (from_city, to_city)
    
    neighbors = roads[end_city]

    if len(neighbors) > 1 or end_city == '1':
        for neighbor in neighbors:
            
            if neighbor != end_city and neighbor != '1':
                if (neighbor, end_city) not in times:
                    times[(neighbor, end_city)] = CityTimes()

                if end_city in path:
                    if path[end_city] != neighbor:
                        path[neighbor] = end_city

                        check_from_city = neighbor
                        check_to_city = path[neighbor]
                        
                        prep_time, speed = city_info[check_from_city]
                            
                        city_after_next = path[check_to_city]

                        if times[(check_to_city, city_after_next)].fastest_from == check_to_city:
                            # checking total time of chain of cities, that takes to get from to_city to optimal city (next_city)
                            # and checking how fast guy from start city (neighbor) can make this
                            
                            
                            curr_optimal_time = 0
                            this_city_guy_time = 0

                            curr_from_city = check_from_city
                            times[(curr_from_city, check_to_city)].fastest_time_to_get_here = prep_time + roads[curr_from_city][check_to_city] / speed
                            times[(curr_from_city, check_to_city)].fastest_from = curr_from_city


                            curr_from_city = check_to_city
                            final_city = path[check_to_city]
                            
                            while times[(curr_from_city, final_city)].fastest_from == check_to_city and final_city != '1':
                                curr_optimal_time += times[(curr_from_city, final_city)].fastest_time_to_get_here
                                this_city_guy_time += roads[curr_from_city][final_city] / speed

                                curr_from_city = final_city
                                final_city = path[final_city]

                            if curr_optimal_time > this_city_guy_time:
                                # set this cities chain time according to guy's city
                                
                                curr_from_city = path[check_from_city]
                                curr_to_city = path[curr_from_city]
                                
                                while curr_from_city != final_city:
                                    times[(curr_from_city, curr_to_city)].fastest_time_to_get_here = roads[curr_from_city][curr_to_city] / speed
                                    times[(curr_from_city, curr_to_city)].fastest_from = check_from_city

                                    curr_from_city = curr_to_city
                                    curr_to_city = path[curr_to_city]

                        


                        else:
                            times[(check_from_city, check_to_city)].fastest_time_to_get_here = prep_time + roads[check_from_city][check_to_city] / speed
                            times[(check_from_city, check_to_city)].fastest_from = check_from_city

                            # old search algo

                            curr_from_city = check_from_city
                            curr_to_city = check_to_city

                            while curr_to_city != '1':
                                this_city_guy_time = roads[curr_from_city][curr_to_city] / speed

                                if times[(curr_from_city, curr_to_city)].fastest_time_to_get_here > this_city_guy_time:
                                    times[(curr_from_city, curr_to_city)].fastest_time_to_get_here = this_city_guy_time
                                    times[(curr_from_city, curr_to_city)].fastest_from = check_from_city

                                    curr_from_city = curr_to_city
                                    curr_to_city = path[curr_to_city]

                                else:
                                    break


                        path[neighbor] = end_city
                        time_searcher(roads, city_info, path, times, end_city=neighbor)
                
                else:
                    # first iteration
                    prep_time, speed = city_info[neighbor]
                    time_from_here_to_neighbor = prep_time + roads[neighbor][end_city] / speed
                    
                    times[(neighbor, end_city)].fastest_time_to_get_here = time_from_here_to_neighbor
                    times[(neighbor, end_city)].fastest_from = neighbor

                    path[neighbor] = end_city
                    time_searcher(roads, city_info, path, times, end_city=neighbor)

    return times
            







f = open('input.txt')
N = f.readline()
N = int(N)

roads = {}

city_info = {}

for city_id in range( 1,N+1 ):
    prep_time, speed = f.readline().split()
    prep_time = int(prep_time)
    speed = int(speed)

    city_info[str(city_id)] = (prep_time, speed)


for _ in range( N-1 ):
    from_id, to_id, dist = f.readline().split()
    dist = int(dist)


    if from_id not in roads:
        roads[from_id] = {}

    if to_id not in roads[from_id]:
        roads[from_id][to_id] = []

    if to_id not in roads:
        roads[to_id] = {}

    if from_id not in roads[to_id]:
        roads[to_id][from_id] = []


    roads[from_id][to_id] = dist
    roads[to_id][from_id] = dist

res = time_searcher(roads, city_info)

graph = {}
for road in res:
    from_city, to_city = road
    
    if from_city not in graph:
        graph[from_city] = {}
    
    if to_city not in graph:
        graph[to_city] = {}

    graph[from_city][to_city] = res[road].fastest_time_to_get_here
    graph[to_city][from_city] = res[road].fastest_time_to_get_here

print(graph)
# # if R < N**2:
R, max_dist, point_w_max_dist = deikstraSearchFast(graph, '1')
print(max_dist, point_w_max_dist)
# # else:
# #     R = deikstraSearchSlow(graph, S, F)

# elif V in R and R[V].arrival_time != math.inf:
#     print(R[V].arrival_time)
