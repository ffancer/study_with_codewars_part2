def multiple(x):
    return "BangBoom" if x % 15 == 0 else "Boom" if x % 5 == 0 else "Bang" if x % 3 == 0 else "Miss"


print(multiple(30), "BangBoom")
print(multiple(3), "Bang")
print(multiple(98), "Miss")
print(multiple(65), "Boom")
print(multiple(23), "Miss")
print(multiple(15), "BangBoom")
