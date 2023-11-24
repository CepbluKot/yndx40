import math


class Point:
    visited = False
    dist = math.inf
    from_point = None


def deikstraSearch(
    graph: dict,
    point_from: str,
    point_to: str,
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

            for neighbor in graph[curr_point]:
                curr_dist = points_data[curr_point].dist + graph[curr_point][neighbor]

                if curr_dist < points_data[neighbor].dist:
                    points_data[neighbor].dist = curr_dist
                    points_data[neighbor].point_from = curr_point

            
            points_data[curr_point].visited = True
        
    return points_data


N, S, F = input().split()

graph = {}

for from_elem_id in range(1, int(N)+1):
    data = list(map(str, input().split()))

    from_elem_id = str(from_elem_id)
    if not from_elem_id in graph:
        graph[from_elem_id] = {}

    for to_elem_id in range(len(data)):
        if data[to_elem_id] != '-1':
            
            graph[from_elem_id][str(to_elem_id + 1)] = int(data[to_elem_id])
    

r = deikstraSearch(graph, S, F)
if r[F].dist != math.inf:
    print(r[F].dist)
else:
    print(-1)