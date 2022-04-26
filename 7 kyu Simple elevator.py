levels = [0, 1, 2, 3]
buttons = ['0', '1', '2', '3']


def goto(level, button):
    if level not in levels or button not in buttons:
        return 0
    else:
        return int(button) - level


print(goto(0, '2'), 2)
print(3 + goto(3, '1'), 1)
print(2 + goto(2, '2'), 2)
