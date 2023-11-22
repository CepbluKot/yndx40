import math
import heapq


class Point:
    visited = False
    dist = math.inf
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
                new_point.dist = 0
            else:
                new_point.dist = graph[point][point_from]

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
                        points_data[neighbor].dist = curr_dist
                        points_data[neighbor].from_point = curr_point
                        heapq.heappush(pts_heap, (points_data[neighbor].dist, neighbor))

                
                points_data[curr_point].visited = True
            
        else:
            all_pts_checked = True

    return points_data


f = open('input.txt')
N, K = f.readline().split()
N, K = int(N), int(K)
graph = {}

if K:
    for _ in range( K ):
        from_id, to_id, length =  f.readline().split()
        length = int(length)
        

        if not from_id in graph:
            graph[from_id] = {}

        if not to_id in graph:
            graph[to_id] = {}

        graph[from_id][to_id] = length
        graph[to_id][from_id] = length
        
    S, F = f.readline().split()


    if K < N**2:
        r = deikstraSearchFast(graph, S, F)
    else:
        r = deikstraSearchSlow(graph, S, F)

    
    if F in r and r[F].dist != math.inf:
        print(r[F].dist)


    else:
        print(-1)
else:
    print(-1)
