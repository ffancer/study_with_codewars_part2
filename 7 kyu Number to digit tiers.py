def create_array_of_tiers(n):
    lst = []

    while n:
        lst.append(str(n))
        n //= 10

    return lst[::-1] or ['0']



print(create_array_of_tiers(420), ["4", "42", "420"])
print(create_array_of_tiers(2017), ["2", "20", "201", "2017"])
print(create_array_of_tiers(2010), ["2", "20", "201", "2010"])
print(create_array_of_tiers(4020), ["4", "40", "402", "4020"])
print(create_array_of_tiers(80200), ["8", "80", "802", "8020", "80200"])
