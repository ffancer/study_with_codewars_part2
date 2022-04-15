# 7 kyu
# Coding 3min: Bug in Apple


def sc(apple):
    return [[i, j.index('B')] for i, j in enumerate(apple) if 'B' in j][0]


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
