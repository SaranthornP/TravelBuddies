import itertools
import sys
import heapq
from Algorithm.Calculate_Distance import *

def calculate_lower_bound(path, distances, remaining_cities):
    lower_bound = 0

    # คำนวณระยะทางที่ต้องการจากเมืองที่อยู่ปัจจุบันไปยังเมืองที่มีระยะทางสั้นที่สุด
    lower_bound += calculate_total_distance(path, distances)

    # คำนวณระยะทางที่ต้องการจากเมืองที่อยู่ปัจจุบันไปยังเมืองที่มีระยะทางสั้นที่สุด (สำหรับตัวอย่างเพื่อนช่วย)
    lower_bound += min(distances[path[-1]][city] for city in remaining_cities)

    return lower_bound

def branch_and_bound_partition(distances):
    n = len(distances)
    all_cities = set(range(n))
    initial_path = [0]
    remaining_cities = set(range(1, n))

    # สร้างโหนดเริ่มต้น
    initial_node = (0, {'path': initial_path, 'lower_bound': 0})

    # ใช้ Priority Queue (Heap) เพื่อเก็บโหนดที่จะสำรวจต่อไป
    nodes_to_explore = [initial_node]

    # บันทึกเส้นทางที่มีระยะทางรวมน้อยที่สุด
    best_path = None
    min_total_distance = float('inf')

    while nodes_to_explore:
        current_node = heapq.heappop(nodes_to_explore)[1]  # เอาโหนดที่มี lower_bound น้อยที่สุดมาทำงานต่อ

        current_path = current_node['path']
        remaining_cities = all_cities - set(current_path)

        # ตรวจสอบว่าเส้นทางปัจจุบันสามารถทำให้ได้เส้นทางที่ดีกว่าได้หรือไม่
        if len(remaining_cities) > 1:
            lower_bound = calculate_lower_bound(current_path, distances, remaining_cities)
            if lower_bound >= min_total_distance:
                continue

        # ถ้าถึงตำแหน่งสุดท้ายแล้ว
        if len(remaining_cities) == 1:
            last_city = remaining_cities.pop()
            current_path.append(last_city)
            current_path.append(current_path[0])  # เพื่อให้เส้นทางปิดลงท้ายที่เมืองแรก
            total_distance = calculate_total_distance(current_path, distances)

            # บันทึกถ้าเส้นทางปัจจุบันดีกว่าเส้นทางที่มีระยะทางรวมน้อยที่สุด
            if total_distance < min_total_distance:
                best_path = current_path
                min_total_distance = total_distance
        else:
            # สร้างโหนดย่อยที่จะสำรวจต่อไป
            for next_city in remaining_cities:
                new_path = current_path + [next_city]
                new_node = (calculate_lower_bound(new_path, distances, remaining_cities), {'path': new_path, 'lower_bound': calculate_lower_bound(new_path, distances, remaining_cities)})
                heapq.heappush(nodes_to_explore, new_node)

    # สร้าง path_b จากเมืองที่ไม่ได้ถูกเลือกไว้ใน path_a
    path_b = [city for city in all_cities if city not in best_path]

    return best_path, path_b, min_total_distance