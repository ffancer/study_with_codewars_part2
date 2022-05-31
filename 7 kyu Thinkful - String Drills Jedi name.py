# 7 kyu
# Thinkful - String Drills: Jedi name


def greet_jedi(first, last):
    return f'Greetings, master {last[:3].title() + first[:2].title()}'


print(greet_jedi('Beyonce', 'Knowles'), 'Greetings, master KnoBe')
print(greet_jedi('Chris', 'Angelico'), 'Greetings, master AngCh')
print(greet_jedi('grae', 'drake'), 'Greetings, master DraGr')
