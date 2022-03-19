def arr2bin(arr):
    return bin(sum(i for i in arr))[2:] if all(type(i) == int for i in arr) else False


print(arr2bin([1, 2]), "11")
print(arr2bin([1, 2, 3, 4, 5]), "1111")
print(arr2bin([1, 10, 100, 1000]), "10001010111")
print(arr2bin([1, 10, 100, 'bb']), "False")
