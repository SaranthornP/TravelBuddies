from Algorithm.Calculate_Distance import *

def greedy_partition(distances):
    n = len(distances)
    all_cities = set(range(n))
    path_a = []
    path_b = []

    # เลือกเมืองแรกไปที่ path_a
    current_city = 0
    path_a.append(current_city)
    all_cities.remove(current_city)

    while all_cities:
        # เลือกเมืองที่มีระยะทางสั้นที่สุดไปยัง path_a
        next_city = min(all_cities, key=lambda city: distances[current_city][city])
        path_a.append(next_city)
        all_cities.remove(next_city)
        current_city = next_city

        if all_cities:
            # เลือกเมืองที่มีระยะทางสั้นที่สุดไปยัง path_b
            next_city = min(all_cities, key=lambda city: distances[current_city][city])
            path_b.append(next_city)
            all_cities.remove(next_city)
            current_city = next_city

    total_distance_path_a = calculate_total_distance(path_a, distances)
    total_distance_path_b = calculate_total_distance(path_b, distances)
    
    return path_a, path_b, total_distance_path_a, total_distance_path_b