# 7 kyu
# Thinkful - List and Loop Drills: Inverse Slicer


def inverse_slice(items, a, b):
    lst = []

    for i in items:
        if i in items[a:b]:
            continue
        else:
            lst.append(i)

    return lst


print(inverse_slice([12, 14, 63, 72, 55, 24], 2, 4), [12, 14, 55, 24])
print(inverse_slice([12, 14, 63, 72, 55, 24], 0, 3), [72, 55, 24])
print(inverse_slice(['Intuition', 'is', 'a', 'poor', 'guide', 'when', 'facing', 'probabilistic', 'evidence'], 5, 13),
      ['Intuition', 'is', 'a', 'poor', 'guide'])
