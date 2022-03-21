def histogram(results):
    lst = []

    for i, j in enumerate(results):
        # print(i, j)
        lst.append(f'{i+1}| {"#" * j} {j}')
    return lst

res = """6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
"""
print(histogram([7, 3, 10, 1, 0, 5]), res)

res = """6|
5|
4|
3|
2|
1|
"""
print(histogram([0, 0, 0, 0, 0, 0]), res)
