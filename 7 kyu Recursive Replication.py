@countcalls
def replicate(times, number):
    if times > 0:
        return [number] + replicate(times - 1, number)
    return []


print(replicate(3, 5), [5, 5, 5])
print(replicate(5, 1), [1, 1, 1, 1, 1])
print(replicate(0, 12), [])
print(replicate(-1, 12), [])
print(replicate(8, 0), [0, 0, 0, 0, 0, 0, 0, 0])
