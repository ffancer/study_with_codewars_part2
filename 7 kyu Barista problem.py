def barista(coffees):
    time, total = 0, 0

    for e in sorted(coffees):
        time += e
        total += time
        time += 2

    return total


print(barista([2, 10, 5, 3, 9]), 85, 'Sorry, but the smallest waiting time possible is: 85')
print(barista([4, 3, 2]), 22, 'Sorry, but the smallest waiting time possible is: 22')
print(barista([20, 5]), 32, 'Sorry, but the smallest waiting time possible is: 32')
print(barista([20, 5, 4, 3, 1, 5, 7, 8]), 211, 'Sorry, but the smallest waiting time possible is: 211')
print(barista([5, 4, 3, 2, 1]), 55, 'Sorry, but the smallest waiting time possible is: 55')
