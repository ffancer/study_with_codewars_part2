def main_diagonal_product(mat):
    for i, j in enumerate(mat):
        print(i, j)


res1 = main_diagonal_product([[1, 0], [0, 1]])
res2 = main_diagonal_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("main_diagonal_product([1,0],[0,1]) => 1")
print(res1, 1)

print("main_diagonal_product([1,2,3],[4,5,6],[7,8,9]) => 45")
print(res2, 45)
