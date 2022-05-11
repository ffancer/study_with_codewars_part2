# 7 kyu
# Is There an Odd Bit?


def any_odd(x):
    x = bin(x)[2:]
    for i in range(len(x)):
        if i % 2 != 0:
            if x[i] == '1':
                return True
    return False



print(any_odd(5), 0)
print(any_odd(170), 1)
print(any_odd(2), 1)
