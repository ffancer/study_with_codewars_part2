def t_area(t_str):
    return t_str.split('\n')[-2].count(' ') * (t_str.count('\n') - 2) / 2


print(t_area('\n.\n. .\n'), .5)
print(t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n'), 8.0)
print(t_area('\n.\n. .\n. . .\n'), 2.0)
print(t_area(
    '\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n'),
    32.0)
