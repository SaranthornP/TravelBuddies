def minTotal(start, mask, distances, memo):
    n = len(distances)
    
    # ถ้า mask เป็นเซ็ตที่มีเมืองทั้งหมดแล้ว
    if mask == (1 << n) - 1:
        return distances[start][0]

    # ถ้าคำนวณแล้ว (memoization)
    if (start, mask) in memo:
        return memo[(start, mask)]

    min_distance = float('inf')

    for next_city in range(n):
        if (mask >> next_city) & 1 == 0:  # ถ้าเมืองนี้ยังไม่ถูกเลือก
            new_mask = mask | (1 << next_city)
            distance = distances[start][next_city] + minTotal(next_city, new_mask, distances, memo)
            min_distance = min(min_distance, distance)

    memo[(start, mask)] = min_distance
    return min_distance

def dynamic_partition(distances):
    n = len(distances)
    all_cities = set(range(n))

    # ใช้ memoization เพื่อลดการคำนวณที่ซ้ำซ้อน
    memo = {}

    # เริ่มต้นที่เมือง 0 และเป็นเซ็ตที่ไม่มีเมืองใดเลือกไว้
    total_distance = minTotal(0, 1, distances, memo)

    # สร้าง path_a จากการติดตาม memoization
    path_a = [0]
    mask = 1

    while mask != (1 << n) - 1:
        next_city = None
        for city in all_cities:
            if (mask >> city) & 1 == 0 and (next_city is None or distances[path_a[-1]][city] + memo[(city, mask | (1 << city))] < distances[path_a[-1]][next_city] + memo[(next_city, mask | (1 << next_city))]):
                next_city = city
        path_a.append(next_city)
        mask |= (1 << next_city)

    # เพื่อให้ path_a เริ่มต้นและลงท้ายที่เมืองเดียวกัน

    # สร้าง path_b จากเมืองที่ไม่ได้ถูกเลือกไว้ใน path_a
    path_b = [city for city in all_cities if city not in path_a]

    return path_a, path_b, total_distance