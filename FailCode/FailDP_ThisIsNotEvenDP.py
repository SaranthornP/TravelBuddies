from sys import maxsize
from itertools import permutations
def tsp(graph, s):
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    min_cost = maxsize
    path = []
    next_permutation=permutations(vertex)
    for i in next_permutation:
        #print(i)
        current_cost = 0
        k = s
        for j in i:
            current_cost += graph[k][j]
            k = j
        min_cost = min(min_cost, current_cost)
        if min_cost == min(min_cost, current_cost): path = i
    min_cost = min_cost - graph[k][s]
    return min_cost, path

graph = [
        [0, 328, 259, 180, 314, 294, 269, 391],
        [328, 0, 83, 279, 107, 131, 208, 136],
        [259, 83, 0, 257, 70, 86, 172, 152],
        [180, 279, 257, 0, 190, 169, 157, 273],
        [314, 107, 70, 190, 0, 25, 108, 182],
        [294, 131, 86, 169, 25, 0, 84, 158],
        [269, 208, 172, 157, 108, 84, 0, 140],
        [391, 136, 152, 273, 182, 158, 140, 0],
    ]
best_cost = 10 ** 9
best_path = []
starter_node = 0
for s in range(len(graph)):
    min_cost, path = tsp(graph, s)
    best_cost = min(min_cost, best_cost)
    if best_cost == min_cost: 
        best_path = path
        starter_node = s
print(best_cost, f"Start from {starter_node} ->", best_path)