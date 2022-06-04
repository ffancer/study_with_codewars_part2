# Remember you have a CHANGE dictionary to work with ;)
CHANGE = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25, 'dollar': 1.0}


def change_count(change):
    total = 0

    for i in change.split():
        total += CHANGE[i]
    return total


print(change_count('dime penny dollar'), '$1.11')
print(change_count('dime penny nickel'), '$0.16')
print(change_count('quarter quarter'), '$0.50')
print(change_count('dollar penny dollar'), '$2.01')
print(change_count('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny'), '$10.01')
