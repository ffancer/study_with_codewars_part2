def barista(coffees):
    clean = 2
    sorted_lst = sorted(coffees)
    a = sorted_lst[0]
    total = 0

    for i in sorted_lst[1:]:
        total += clean + a + i
        a = i

    return total



print(barista([2, 10, 5, 3, 9]), 85, 'Sorry, but the smallest waiting time possible is: 85')
print(barista([4, 3, 2]), 22, 'Sorry, but the smallest waiting time possible is: 22')
print(barista([20, 5]), 32, 'Sorry, but the smallest waiting time possible is: 32')
print(barista([20, 5, 4, 3, 1, 5, 7, 8]), 211, 'Sorry, but the smallest waiting time possible is: 211')
print(barista([5, 4, 3, 2, 1]), 55, 'Sorry, but the smallest waiting time possible is: 55')