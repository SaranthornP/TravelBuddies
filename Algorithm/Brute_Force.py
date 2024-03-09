import itertools
from Algorithm.Calculate_Distance import *

def find_optimal_partition(distances):
    n = len(distances)
    all_cities = set(range(n))
    min_total_distance = float('inf')
    optimal_partition = None

    for partition in itertools.combinations(all_cities, n // 2):
        remaining_cities = all_cities - set(partition)
        path_a = list(partition)
        path_b = list(remaining_cities)

        total_distance = calculate_total_distance(path_a, distances) + \
                         calculate_total_distance(path_b, distances)

        if total_distance < min_total_distance:
            min_total_distance = total_distance
            optimal_partition = (path_a, path_b)
    return optimal_partition, min_total_distance