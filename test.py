n = 4  # there are ten nodes in the example graph (graph is 1-based)

# dist[i][j] represents the shortest distance to go from i to j
# this matrix can be calculated for any given graph using 
# all-pair shortest path algorithms
dist = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]

# memoization for top-down recursion
memo = [[[-1] * (1 << (n + 1)) for _ in range(2)] for _ in range(n + 1)]

# path to store the optimal path
path = [[[] for _ in range(1 << (n + 1))] for _ in range(n + 1)]


def fun(i, mask, person):
    # base case
    # if only the ith bit and 1st bit is set in our mask,
    # it implies we have visited all other nodes already
    if mask == ((1 << i) | 3):
        path[i][mask] = [1, i]
        return dist[1][i]

    # memoization
    if memo[i][person][mask] != -1:
        return memo[i][person][mask]

    res = 10 ** 9  # result of this sub-problem

    # we have to travel all nodes j in mask and end the path at ith node
    # so for every node j in mask, recursively calculate the cost of
    # traveling all nodes in mask
    # except i and then travel back from node j to node i taking
    # the shortest path, take the minimum of all possible j nodes
    for j in range(1, n + 1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            temp_res = fun(j, mask & (~(1 << i)), person) + dist[j][i]
            if temp_res < res:
                res = temp_res
                path[i][mask] = path[j][mask & (~(1 << i))] + [i]

    memo[i][person][mask] = res  # storing the minimum value
    return res


# Driver program to test above logic
ans = 10 ** 9
start_city = -1
start_person = -1

for person in range(2):
    for i in range(1, n + 1):
        # try to go from node 1 visiting all nodes in between to i
        # then return from i taking the shortest route to 1
        temp_res = fun(i, (1 << (n + 1)) - 1, person)
        if temp_res < ans:
            ans = temp_res
            start_city = i
            start_person = person

# Display the cost of the most efficient tour
print("The cost of the most efficient tour =", ans)

# Display the optimal path for both persons
print("Optimal path for Person 1:", path[start_city][(1 << (n + 1)) - 1])
print("Optimal path for Person 2:", [x for x in range(1, n + 1) if x not in path[start_city][(1 << (n + 1)) - 1]])
