def arr2bin(arr):
    ans = 0

    for i in arr:
        if type(i) != int:
            return False
        ans += i

    return bin(ans)[2:]


print(arr2bin([1, 2]), "11")
print(arr2bin([1, 2, 3, 4, 5]), "1111")
print(arr2bin([1, 10, 100, 1000]), "10001010111")
