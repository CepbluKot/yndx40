import math
import heapq


class Point:
    visited = False
    arrival_time = math.inf
    from_point = None


def deikstraSearchSlow(
    graph: dict,
    point_from: str,
    point_to: str,
):
    points_data = {}

    for point in graph:
        new_point = Point()
        if point == point_from:
            if not point_from in graph[point]:
                new_point.dep_time = 0
            else:
                new_point.dep_time = graph[point][point_from]

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

            for neighbor in graph[curr_point]:
                curr_dist = points_data[curr_point].dist + graph[curr_point][neighbor]

                if curr_dist < points_data[neighbor].dist:
                    points_data[neighbor].dist = curr_dist
                    points_data[neighbor].from_point = curr_point

            
            points_data[curr_point].visited = True
        
    return points_data


def deikstraSearchFast(
    graph: dict,
    point_from: str,
    point_to: str,
):
    points_data = {}
    
    
    pts_heap = []
    heapq.heapify(pts_heap)


    for point in graph:
        new_point = Point()
        if point == point_from:
            new_point.arrival_time = 0

        points_data[point] = new_point
        heapq.heappush(pts_heap, (new_point.arrival_time, point))

        for neighbor_point in graph[point]:
            new_point = Point()
            
            if neighbor_point not in points_data:
                points_data[neighbor_point] = new_point
                heapq.heappush(pts_heap, (new_point.arrival_time, neighbor_point))




    all_pts_checked = False
    while not all_pts_checked:
        all_pts_checked = True
        if pts_heap:
            all_pts_checked = False
            curr_point = heapq.heappop(pts_heap)[1]
            if not points_data[curr_point].visited:

                if curr_point in graph:
                    for neighbor in graph[curr_point]:
                        for neighbor_raise in graph[curr_point][neighbor]:

                            departure_time = neighbor_raise[0]
                            arrival_time = neighbor_raise[1]

                            if departure_time >= points_data[curr_point].arrival_time:
                                if arrival_time < points_data[neighbor].arrival_time:
                                    points_data[neighbor].arrival_time = arrival_time
                                    points_data[neighbor].from_point = curr_point
                                    heapq.heappush(pts_heap, (points_data[neighbor].arrival_time, neighbor))

                    
                    points_data[curr_point].visited = True
            
        else:
            all_pts_checked = True

    return points_data


f = open('input.txt')
N = f.readline()
N = int(N)

D, V = f.readline().split()
R = f.readline()
R = int(R)


graph = {}

for _ in range( R ):
    from_id, departure_time, to_id, arrival_time =  f.readline().split()

    departure_time = int(departure_time)
    arrival_time = int(arrival_time)
    
    if from_id not in graph:
        graph[from_id] = {}

    if to_id not in graph[from_id]:
        graph[from_id][to_id] = []

    graph[from_id][to_id].append( (departure_time, arrival_time))


# if R < N**2:
R = deikstraSearchFast(graph, D, V)
# else:
#     R = deikstraSearchSlow(graph, S, F)

if V == D:
    print(0)

elif V in R and R[V].arrival_time != math.inf:
    print(R[V].arrival_time)


else:
    print(-1)