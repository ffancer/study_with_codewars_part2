def elimination(arr):
    try:
        return int(''.join(str(i) for i in arr if arr.count(i) == 2)[0])
    except IndexError:
        return None


print(elimination([2, 5, 34, 1, 22, 1]), 1, "twins are 1s")
print(elimination([2, 2, 34, 1, 22]), 2, "twins are 2s")
print(elimination([2, 5, 34, 1, 22]), None, "There are no twins in the city")
