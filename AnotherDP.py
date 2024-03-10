import itertools

def tsp(city_count, distances):
    # Generate all possible city permutations
    all_cities = set(range(city_count))
    all_permutations = itertools.permutations(all_cities)

    # Initialize minimum distance to a large value
    min_distance = float('inf')

    # Iterate through all permutations and split the cities into two lists
    for permutation in all_permutations:
        for split_point in range(1, city_count):
            list_a = permutation[:split_point]
            list_b = permutation[split_point:]

            # Calculate the total distance for both lists
            total_distance_a = sum(distances[list_a[i]][list_a[i + 1]] for i in range(len(list_a) - 1))
            total_distance_b = sum(distances[list_b[i]][list_b[i + 1]] for i in range(len(list_b) - 1))

            # Update minimum distance if the current split is better
            current_distance = total_distance_a + total_distance_b
            if current_distance < min_distance:
                min_distance = current_distance
                best_split = (list_a, list_b)

    return min_distance, best_split

# Example usage
n = 4  # Replace with your desired value of n
distances = [
    [0, 1, 2, 3],  # Replace with your distance matrix
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]

min_distance, best_split = tsp(n, distances)

print("Minimum total distance:", min_distance)
print("Best split:", best_split)
