# 7 kyu
# Thinkful - Number Drills: Congo warehouses
from math import ceil


def box_capacity(length, width, height):
    boxes_len = length / 1.3
    boxes_wid =  width / 1.3
    boxes_hgt =  height/ 1.3
    return boxes_len * boxes_wid * boxes_hgt


print(box_capacity(32, 64, 16), 13824)
print(box_capacity(20, 20, 20), 3375)
print(box_capacity(80, 40, 20), 27000)
