def scoreboard(string):
    dct = {
        'nil': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }


print(scoreboard("The score is four nil"), [4, 0])
print(scoreboard("new score: two three"), [2, 3])
print(scoreboard("two two"), [2, 2])
print(scoreboard("Arsenal just conceded another goal, two nil"), [2, 0])
