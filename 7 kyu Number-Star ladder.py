def pattern(n):
    s = ''

    for i in range(1, n + 1):
        if i == 1:
            s += f'{i}\n'
        else:
            s += f'{1}{"*" * (i - 1)}{i}\n'

    return s[:-1]


print(pattern(3), "1\n1*2\n1**3")
print(pattern(7), "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7")
print(pattern(20),
      "1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7\n1*******8\n1********9\n1*********10\n1**********11\n1***********12\n1************13\n1*************14\n1**************15\n1***************16\n1****************17\n1*****************18\n1******************19\n1*******************20")