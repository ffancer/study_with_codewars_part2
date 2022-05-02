def number_property(n):
    lst = []


    def is_prime(n):
        if n > 1:
            for i in range(2, int(n / 2) + 1):
                if (n % i) == 0:
                    lst.append(False)
                    break
            else:
                lst.append(True)
        else:
            print(lst.append(False))
    is_prime(n)

    if n % 2 == 0:
        lst.append(True)
    else:
        lst.append(False)

    return lst

print(number_property(-10), [False, True, True])
print(number_property(2), [True, True, False])
print(number_property(120), [False, True, True])
print(number_property(125), [False, False, False])
