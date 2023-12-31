import math
import  sys
sys.setrecursionlimit(2000)

class Point:
    visited = False
    dist = math.inf
    from_point = None


def deikstraSearch(
    graph: dict,
    point_from: str,

):
    points_data = {}
    for point in graph:
        new_point = Point()
        if point == point_from:
            new_point.dist = 0
        
        points_data[point] = new_point

    all_pts_checked = False
    while not all_pts_checked:
        all_pts_checked = True

        for point in points_data:
            if not points_data[point].visited:
                curr_point = point
                all_pts_checked = False
                break

        if not all_pts_checked:

            for point in points_data:
                if points_data[point].dist < points_data[curr_point].dist and not points_data[point].visited:
                    curr_point = point

            if curr_point in graph:
                for neighbor in graph[curr_point]:
                    curr_dist = points_data[curr_point].dist + graph[curr_point][neighbor]

                    if neighbor not in points_data:
                        points_data[neighbor] = Point()

                    if curr_dist < points_data[neighbor].dist:
                        points_data[neighbor].dist = curr_dist
                        points_data[neighbor].from_point = curr_point

            

            points_data[curr_point].visited = True
        
    return points_data


def find_time_to_neighbors(origin_city, from_city, prev_time: int, speed: int, roads: dict, times: dict):

    if from_city != '1':
        for to_city in roads[from_city]:
            if to_city != from_city and to_city != origin_city: # check if dead end
                if to_city not in times:
                    times[to_city] = {}
                if origin_city not in times[to_city]:
                    times[to_city][origin_city] = prev_time + roads[to_city][from_city] / speed


                    find_time_to_neighbors(origin_city, to_city, times[to_city][origin_city], speed, roads, times)


def time_searcher(roads: dict, city_info: dict, times: dict={}, visited_cities: set=set()):
    # times: key = (from_city, to_city)
    
    # bfs: first step = start time + dist
    # next ones: prev + dist

    for from_city in roads:
        if from_city not in visited_cities and from_city != '1':
            prep_time, speed = city_info[from_city]
            prev_time = 0

            for to_city in roads[from_city]:
                if to_city not in times:
                    times[to_city] = {}

                if from_city not in times[to_city]:         
                    times[to_city][from_city] = prep_time + roads[to_city][from_city] / speed
                    
                    prev_time = times[to_city][from_city]
            
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
        roads[from_id][to_id] = None

    if to_id not in roads:
        roads[to_id] = {}

    if from_id not in roads[to_id]:
        roads[to_id][from_id] = None


    roads[from_id][to_id] = dist
    roads[to_id][from_id] = dist


res = time_searcher(roads, city_info)

max_pt = None
max_d = 0
points_data = deikstraSearch(res, '1')

for point in points_data:
    if max_d < points_data[point].dist:

        max_d = points_data[point].dist
        max_pt = point


restored_path = [max_pt]
curr_point = points_data[max_pt].from_point
while curr_point:
    restored_path.append(curr_point)
    curr_point = points_data[curr_point].from_point


print(max_d)
print(*restored_path)
# print('done in ', time.time()-start)