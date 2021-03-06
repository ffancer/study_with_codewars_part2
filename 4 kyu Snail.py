def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(array), expected)

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail(array), expected)
