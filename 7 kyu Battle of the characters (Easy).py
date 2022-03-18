"""
Сегодня мой отец умер, в 6 утра. Пусть эта информация затеряется здесь, словно капля во время дождя.
Сижу и продолжаю решать задачи.
"""

def battle(x, y):
    cnt_x, cnt_y = 0, 0

    cnt_x = sum(ord(i) - 64 for i in x)
    cnt_y = sum(ord(i) - 64 for i in y)

    return x if cnt_x > cnt_y else y if cnt_y > cnt_x else 'Tie!'


print(battle("AAA", "Z"), "Z", "Unfair fight!")
print(battle("ONE", "TWO"), "TWO", "Unfair fight!")
print(battle("ONE", "NEO"), "Tie!", "Unfair fight!")
print(battle("FOUR", "FIVE"), "FOUR", "Unfair fight!")
