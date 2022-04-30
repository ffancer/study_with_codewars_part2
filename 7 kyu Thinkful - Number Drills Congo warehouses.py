# 7 kyu
# Thinkful - Number Drills: Congo warehouses


def box_capacity(length, width, height):
    boxes_len = 1.3 * length
    boxes_wid = 1.3 * width
    boxes_hgt = 1.3 * height
    return boxes_len, boxes_wid, boxes_hgt


print(box_capacity(32, 64, 16), 13824)
print(box_capacity(20, 20, 20), 3375)
print(box_capacity(80, 40, 20), 27000)
