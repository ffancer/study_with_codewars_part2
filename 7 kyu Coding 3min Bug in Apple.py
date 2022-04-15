# 7 kyu
# Coding 3min: Bug in Apple


def sc(apple):
    lst = []

    for i,j in enumerate(apple):
        if 'B' in j:
            lst.append(i)
            lst.append(j.index('B'))

    return lst

apple = [
    ["B", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"]
]
answer = [0, 0]
print(sc(apple), answer, "good luck!")

apple = [
    ["A", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"]
]
answer = [1, 1]
print(sc(apple), answer, "good luck!")

apple = [
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"]
]
answer = [4, 1]
print(sc(apple), answer, "good luck!")
