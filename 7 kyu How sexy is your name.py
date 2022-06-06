# 7 kyu
# How sexy is your name?


SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
          'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
          'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}


def sexy_name(name):
    total = 0
    name = ''.join(i.upper() for i in name)

    for i in name:
        if i == ' ':
            continue
        total += SCORES[i]

    return 'NOT TOO SEXY' if total <= 60 else 'PRETTY SEXY' if 61 <= total <= 300 else 'VERY SEXY' if 301 <= total <= 599 else 'THE ULTIMATE SEXIEST'


print(sexy_name('GUV'), 'NOT TOO SEXY')
print(sexy_name('PHUG'), "NOT TOO SEXY")
print(sexy_name('FFFFF'), 'NOT TOO SEXY')
print(sexy_name(''), "NOT TOO SEXY")
print(sexy_name('PHUG'), "NOT TOO SEXY")
print(sexy_name('BOB'), "PRETTY SEXY")
print(sexy_name('JLJ'), 'PRETTY SEXY')
print(sexy_name('HHHHHU'), 'PRETTY SEXY')
print(sexy_name('BOB'), "PRETTY SEXY")
print(sexy_name('WWWWWU'), "PRETTY SEXY")
print(sexy_name('YOU'), 'VERY SEXY')
print(sexy_name('FABIO'), "VERY SEXY")
print(sexy_name('ARUUUUUUUUU'), 'VERY SEXY')
print(sexy_name('ROBBY'), 'THE ULTIMATE SEXIEST')
print(sexy_name('SAMANTHA'), 'THE ULTIMATE SEXIEST')
print(sexy_name('DONALD TRUMP'), "THE ULTIMATE SEXIEST")
print(sexy_name('BILL GATES'), "THE ULTIMATE SEXIEST")
print(sexy_name('SCARLETT JOHANSSON'), "THE ULTIMATE SEXIEST")
print(sexy_name('CODEWARS'), "THE ULTIMATE SEXIEST")
print(sexy_name('PAMELA ANDERSON'), "THE ULTIMATE SEXIEST")
print(sexy_name('you'), 'VERY SEXY')
print(sexy_name('Codewars'), "THE ULTIMATE SEXIEST")
