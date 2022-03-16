def odd_one(arr):
    for i, j in enumerate(arr):
        if j % 2 != 0:
            return i
    return -1


# test.it("Expected '[2,4,6,7,10]' = 3")
print(odd_one([2, 4, 6, 7, 10]), 3)
# test.it("Expected '[2,16,98,10,13,78]' = 4")
print(odd_one([2, 16, 98, 10, 13, 78]), 4)
# test.it("Expected '[4,-8,98,-12,-7,90,100]' = 4")
print(odd_one([4, -8, 98, -12, -7, 90, 100]), 4)
# test.it("Expected '[2,4,6,8]' = -1")
print(odd_one([2, 4, 6, 8]), -1)
