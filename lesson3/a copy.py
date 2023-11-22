import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances






N, K = input().split()
N, K = int(N), int(K)
example_graph = {}

if K:
    for _ in range( K ):
        from_id, to_id, length =  input().split()
        length = int(length)
        

        if not from_id in example_graph:
            example_graph[from_id] = {}

        if not to_id in example_graph:
            example_graph[to_id] = {}

        example_graph[from_id][to_id] = length
        example_graph[to_id][from_id] = length
        
    S, F = input().split()



    print(calculate_distances(example_graph, S)[F])

else:
    print(-1)
