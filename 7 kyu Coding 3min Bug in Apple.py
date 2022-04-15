# 7 kyu
# Coding 3min: Bug in Apple


def sc(apple):
    pass


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
