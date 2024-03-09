import time
import timeit
import itertools
from heapq import heappop, heappush
from Algorithm.Calculate_Distance import *
from Algorithm.Brute_Force import *
from Algorithm.Greedy import *
from Algorithm.Dynamic_Programming import *
from Algorithm.Branch_and_Bound import *

distances = [[0, 5, 8, 12, 3, 7, 10, 15, 9, 6],
 [5, 0, 4, 9, 13, 6, 11, 8, 14, 10],
 [8, 4, 0, 6, 10, 12, 7, 13, 9, 15],
 [12, 9, 6, 0, 11, 14, 5, 8, 7, 13],
 [3, 13, 10, 11, 0, 8, 14, 9, 6, 7],
 [7, 6, 12, 14, 8, 0, 10, 4, 11, 15],
 [10, 11, 7, 5, 14, 10, 0, 13, 8, 9],
 [15, 8, 13, 8, 9, 4, 13, 0, 12, 6],
 [9, 14, 9, 7, 6, 11, 8, 12, 0, 5],
 [6, 10, 15, 13, 7, 15, 9, 6, 5, 0]]           

loop = 1000

#Start finding minimum distance path using different algorithm
print("*"*5, "Starting Calculate", "*"*5, '\n')
print("[Brute Force]")
optimal_partition, min_total_distance = find_optimal_partition(distances)
BF_runtime = timeit.timeit('find_optimal_partition(distances)', globals=globals(), number=loop)
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
path_a, path_b, min_total_distance = dynamic_partition(distances)
DA_runtime = timeit.timeit('dynamic_partition(distances)', globals=globals(), number=loop)
print("Path A:", path_a, "Min Total Distance:", calculate_total_distance(path_a, distances))
print("Path B:", path_b, "Min Total Distance:", calculate_total_distance(path_b, distances))
print("Runtime:", DA_runtime)

path_a, path_b, min_total_distance = branch_and_bound_partition(distances)
BAB_runtime = timeit.timeit('branch_and_bound_partition(distances)', globals=globals(), number=loop)
print("Path A:", path_a, "Min Total Distance:", calculate_total_distance(path_a, distances))
print("Path B:", path_b, "Min Total Distance:", calculate_total_distance(path_b, distances))
print("Runtime:", BAB_runtime)