from Algorithm.Calculate_Distance import *
from itertools import permutations

def find_min_distance_split(n, distances):
    cities = list(range(n))
    all_paths = permutations(cities)

    min_total_distance = float('inf')
    best_split = None

    for path in all_paths:
        for split_point in range(1, n):
            A = path[:split_point]
            B = path[split_point:]
            total_distance_A = calculate_total_distance(A, distances)
            total_distance_B = calculate_total_distance(B, distances)

            total_distance = total_distance_A + total_distance_B

            if total_distance < min_total_distance:
                min_total_distance = total_distance
                best_split = (A, B)

    return best_split, min_total_distance
