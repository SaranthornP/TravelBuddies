import time
import timeit
import itertools
from heapq import heappop, heappush
from Algorithm.Calculate_Distance import *
from Algorithm.Brute_Force import *
from Algorithm.Greedy import *
from Algorithm.Dynamic_Programming import *
from Algorithm.Branch_and_Bound import *

distances =[
        [0, 1, 2, 3],
        [1, 0, 4, 5],
        [2, 4, 0, 6],
        [3, 5, 6, 0]
    ] 
loop = 100

#Start finding minimum distance path using different algorithm
print("*"*5, "Starting Calculate", "*"*5, '\n')
print("[Brute Force]")
optimal_partition, min_total_distance = find_min_distance_split(len(distances) ,distances)
BF_runtime = timeit.timeit('find_min_distance_split(len(distances), distances)', globals=globals(), number=loop)
print("Path A:", optimal_partition[0], "Min Total Distance:", calculate_total_distance(optimal_partition[0], distances))
print("Path B:", optimal_partition[1], "Min Total Distance:", calculate_total_distance(optimal_partition[1], distances))
print("Runtime:", BF_runtime)

print("\n"+"*"*30+"\n")
print("[Greedy Algorithm]")
path_a, path_b, total_distance_path_a, total_distance_path_b = greedy_partition(distances)
GD_runtime = timeit.timeit('greedy_partition(distances)', globals=globals(), number=loop)
print("Path A:", path_a, "Min Total Distance:", total_distance_path_a)
print("Path B:", path_b, "Min Total Distance:", total_distance_path_b)
print("Runtime:", GD_runtime)

print("\n"+"*"*30+"\n")
print("[Dynamic Programming Algorithm]")
FirstPath, SecondPath, SumCost = dpInit(distances)
DA_runtime = timeit.timeit('dpInit(distances)', globals=globals(), number=loop)
print("Split Shortest paths:", FirstPath, SecondPath)
print("Minimum sum of split paths:", SumCost)
print("Runtime:", DA_runtime)
