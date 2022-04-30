# 7 kyu
# Thinkful - Number Drills: Congo warehouses


def box_capacity(length, width, height):
    return (length * 12 // 16) * (width * 12 // 16) * (height * 12 // 16)


print(box_capacity(32, 64, 16), 13824)
print(box_capacity(20, 20, 20), 3375)
print(box_capacity(80, 40, 20), 27000)
