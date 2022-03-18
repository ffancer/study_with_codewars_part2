def battle(x, y):
    cnt_x, cnt_y = 0, 0
    cnt_x = sum(ord(i) - 64 for i in x)
    print(cnt_x)


print(battle("AAA", "Z"), "Z", "Unfair fight!")
print(battle("ONE", "TWO"), "TWO", "Unfair fight!")
print(battle("ONE", "NEO"), "Tie!", "Unfair fight!")
print(battle("FOUR", "FIVE"), "FOUR", "Unfair fight!")
