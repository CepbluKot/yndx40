import math
import heapq


class Point:
    visited = False
    dist = math.inf
    from_point = None


def deikstraSearchFast(
    graph: dict,
    point_from: str
):
    points_data = {}
    # max_dist = 0

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
                        # if curr_dist > max_dist:
                        #     max_dist = curr_dist
                        #     point_w_max_dist = neighbor
                        
                        points_data[neighbor].dist = curr_dist
                        points_data[neighbor].from_point = curr_point
                        heapq.heappush(pts_heap, (points_data[neighbor].dist, neighbor))

                
                points_data[curr_point].visited = True
            
        else:
            all_pts_checked = True

    return points_data



def find_time_to_neighbors(origin_city, from_city, prev_time: int, speed: int, roads: dict, times: dict):
    # ! mb bug at prev_time counter 
    if from_city != '1':
        for to_city in roads[from_city]:
            if to_city != from_city and to_city != origin_city: # check if dead end
                if (origin_city, to_city) not in times:
                    times[(origin_city, to_city)] = prev_time + roads[from_city][to_city] / speed


                    find_time_to_neighbors(origin_city, to_city, times[(origin_city, to_city)], speed, roads, times)

    # return times

def time_searcher(roads: dict, city_info: dict, times: dict={}, visited_cities: set=set()):
    # times: key = (from_city, to_city)
    
    # bfs: first step = start time + dist
    # next ones: prev + dist

    for from_city in roads:
        if from_city not in visited_cities and from_city != '1':
            prep_time, speed = city_info[from_city]
            prev_time = 0

            for to_city in roads[from_city]:
                if (from_city, to_city) not in times:         
                    times[(from_city, to_city)] = prep_time + roads[from_city][to_city] / speed
                    
                    prev_time = times[(from_city, to_city)]
            
                    find_time_to_neighbors(from_city, to_city, prev_time, speed, roads, times)


            visited_cities.add(from_city)

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

graph = {'1':{}}
for road in res:
    from_city, to_city = road
    
    if from_city not in graph:
        graph[from_city] = {}
    

    graph[from_city][to_city] = res[road]

max_pt = None
max_d = 0
max_pts_data = None
for city_id in range( 2,N+1 ):
    points_data = deikstraSearchFast(graph, str(city_id))
    if max_d < points_data['1'].dist:
        max_pts_data = points_data
        max_d = points_data['1'].dist
        max_pt = str(city_id)


restored_path = [1]
curr_point = max_pts_data['1'].from_point
while curr_point:
    restored_path.append(curr_point)
    curr_point = max_pts_data[curr_point].from_point

print(max_d)
print(*restored_path[::-1])
