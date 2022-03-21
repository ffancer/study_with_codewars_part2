def histogram(results):
    lst = []

    for i, j in enumerate(results):
        if j == 0:
            lst.append(f'{i+1}|')
        else:
            lst.append(f'{i+1}|{"#" * j} {j}')

    return '\n'.join(lst[::-1]) + '\n'


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
