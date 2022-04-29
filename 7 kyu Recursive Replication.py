def replicate(times, number):
    return [number] * times


print(replicate(3, 5), [5, 5, 5])
print(replicate(5, 1), [1, 1, 1, 1, 1])
print(replicate(0, 12), [])
print(replicate(-1, 12), [])
print(replicate(8, 0), [0, 0, 0, 0, 0, 0, 0, 0])
