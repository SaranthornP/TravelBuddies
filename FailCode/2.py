from itertools import permutations
def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

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

# Example usage:
distances =  [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]
n = len(distances)

best_split, min_distance = find_min_distance_split(n, distances)

print("Best Split:", best_split)
print("Minimum Total Distance:", min_distance)
