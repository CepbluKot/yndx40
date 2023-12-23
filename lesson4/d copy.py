# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
from itertools import permutations

n = int(input())

V = n

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight) 
		
	return min_path 


graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
      

if n > 2:
    all_except_0_are_0 = True
    for d in range(1, len(graph)):
        for s_id in range(1, len(graph[d])):
            if graph[d][s_id] != 0:
                all_except_0_are_0 = False
                break


    if not all_except_0_are_0:
        print(travellingSalesmanProblem(graph, 0))
        
    else:
        print(-1)

elif n > 1:
    print(travellingSalesmanProblem(graph, 0))
else:
    print(0)
