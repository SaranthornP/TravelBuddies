from Algorithm.Calculate_Distance import *

class TravellingSalesmanProblem:
    def __init__(self, distance, start, cities_count):
        self.distance_matrix = distance
        self.start_city = start
        self.total_cities = len(distance)
        self.cities_count = cities_count
        
        self.end_state = (1 << self.total_cities) - 1
        self.memo = [[None for _col in range(1 << self.total_cities)] for _row in range(self.total_cities)]

        self.shortest_path = []
        self.min_path_cost = float('inf')

    def solve(self):
        self.__initialize_memo()

        for num_element in range(3, self.total_cities + 1):

            for subset in self.__initiate_combination(num_element):

                if self.__is_not_in_subset(self.start_city, subset):
                    continue

                for next_city in range(self.total_cities):

                    if next_city == self.start_city or self.__is_not_in_subset(next_city, subset):
                        continue

                    subset_without_next_city = subset ^ (1 << next_city)
                    min_distance = float('inf')

                    for last_city in range(self.total_cities):
                        if last_city == self.start_city or \
                                last_city == next_city or \
                                self.__is_not_in_subset(last_city, subset):
                            continue

                        new_distance = \
                            self.memo[last_city][subset_without_next_city] + self.distance_matrix[last_city][next_city]

                        if new_distance < min_distance:
                            min_distance = new_distance

                    self.memo[next_city][subset] = min_distance
        self.__calculate_min_cost()
        self.__find_shortest_path()


    def __calculate_min_cost(self):
        for i in range(self.total_cities):

            if i == self.start_city:
                continue

            path_cost = self.memo[i][self.end_state]

            if path_cost < self.min_path_cost:
                self.min_path_cost = path_cost

    def __find_shortest_path(self):
        state = self.end_state
        for i in range(1, self.cities_count):
            best_index = -1
            best_distance = float('inf')
            for j in range(self.total_cities):

                if j == self.start_city or self.__is_not_in_subset(j, state):
                    continue

                new_distance = self.memo[j][state]
                print(i,j,new_distance)
                if new_distance <= best_distance:
                    best_index = j
                    best_distance = new_distance
                    print("best:", best_distance)
                
            self.shortest_path.append(best_index)
            state = state ^ (1 << best_index)
        self.shortest_path.append(self.start_city)
        self.shortest_path.reverse()

    def __initialize_memo(self):
        for destination_city in range(self.total_cities):

            if destination_city == self.start_city:
                continue

            self.memo[destination_city][1 << self.start_city | 1 << destination_city] = \
                self.distance_matrix[self.start_city][destination_city]

    def __initiate_combination(self, num_element):
        subset_list = []
        self.__initialize_combination(0, 0, num_element, self.total_cities, subset_list)
        return subset_list

    def __initialize_combination(self, subset, at, num_element, total_cities, subset_list):

        elements_left_to_pick = total_cities - at
        if elements_left_to_pick < num_element:
            return

        if num_element == 0:
            subset_list.append(subset)
        else:
            for i in range(at, total_cities):
                subset |= 1 << i
                self.__initialize_combination(subset, i + 1, num_element - 1, total_cities, subset_list)
                subset &= ~(1 << i)

    @staticmethod
    def __is_not_in_subset(element, subset):
        return ((1 << element) & subset) == 0
    def optimize_divide_and_conquer(self, path, cost):
        if len(path) <= 2:
            return path, cost

        min_sum = float('inf')
        best_split = None

        for split_point in range(1, len(path)):
            path1 = path[:split_point]
            path2 = path[split_point:]

            sum_cost = sum(self.distance_matrix[path1[i]][path1[i + 1]] for i in range(len(path1) - 1)) + \
                       self.distance_matrix[path1[-1]][path2[0]] + \
                       sum(self.distance_matrix[path2[i]][path2[i + 1]] for i in range(len(path2) - 1))

            if sum_cost < min_sum:
                min_sum = sum_cost
                best_split = (path1, path2)

        if best_split:
            path1, cost1 = self.optimize_divide_and_conquer(best_split[0], min_sum)
            path2, cost2 = self.optimize_divide_and_conquer(best_split[1], min_sum)

            return path1 + path2[1:], cost1 + cost2

        return path, cost

def split_shortest_path(path, distance):
    minimum = 10 ** 9
    PathA = PathB = []
    for i in range(1, len(path)):
        first_path = path[:i]
        second_path = path[i:]
        if minimum > calculate_total_distance(first_path, distance) + calculate_total_distance(second_path, distance):
            minimum = calculate_total_distance(first_path, distance) + calculate_total_distance(second_path, distance)
            PathA = first_path
            PathB = second_path
            
    return PathA, PathB, minimum
        
    
def dpInit(distance_matrix):
    n = len(distance_matrix)
    BestPath = MinimumCost = float('inf')
    for cities_count in range(4, n//2 - n%2, -1):
        for i in range(0, 1):
            start_city = i

            tour = TravellingSalesmanProblem(distance_matrix, start_city, cities_count)
            tour.solve()
            if MinimumCost > tour.min_path_cost:
                MinimumCost = tour.min_path_cost
                BestPath = tour.shortest_path
            
    FirstPath, SecondPath, SumCost = split_shortest_path(BestPath, distance_matrix)
    return FirstPath, SecondPath, SumCost
    print("Split Shortest paths:", FirstPath, SecondPath)
    print("Minimum sum of split paths:", SumCost)