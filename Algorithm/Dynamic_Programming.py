def minTotal(start, mask, distances, memo):
    n = len(distances)

#ถ้า mask เป็นเซ็ตที่มีเมืองทั้งหมดแล้ว
    if mask == (1 << n) - 1:
        return distances[start][0]

    # ถ้าคำนวณแล้ว (memoization)
    if (start, mask) in memo:
        return memo[(start, mask)]

    mindistance = float('inf')

    for next_city in range(n):
        if (mask >> next_city) & 1 == 0:  # ถ้าเมืองนี้ยังไม่ถูกเลือก
            new_mask = mask | (1 << next_city)
            distance = distances[start][next_city] + minTotal(next_city, new_mask, distances, memo)
            min_distance = min(min_distance, distance)

    memo[(start, mask)] = min_distance
    return min_distance

def dynamic_partition(distances):
    n = len(distances)
    dp = [[float('inf')] * (2**n) for i in range(n)]

    # Base case: cost of visiting no city is 0
    dp[0][0] = 0

    # Fill the dp array
    for mask in range(1, 2*n):
        for city in range(n):
            if mask & (1 << city):
                prev_mask = mask ^ (1 << city)
                for prev_city in range(n):
                    if prev_mask & (1 << prev_city):
                        dp[city][mask] = min(dp[city][mask], dp[prev_city][prev_mask] + distances[prev_city][city])

    # Find the minimum cost and the optimal division
    min_cost = min(dp[city][-1] for city in range(n))
    path_a = []
    path_b = []
    mask_a = 0
    for city in range(n):
        if dp[city][-1] == min_cost:
            mask_a = (1 << city)
            break
    for mask in range(1, 2*n):
        if dp[0][mask] == min_cost:
            mask_a = mask
            break
    for city in range(n):
        mask = 1 << city
        if mask_a & mask:
            path_a.append(city)
        else:
            path_b.append(city)

    return path_a, path_b, min_cost