def odd_ones_out(numbers):
    for i in numbers:
        print(i, numbers.count(i))


print(odd_ones_out([1, 2, 3, 1, 3, 3]), [1, 1])
print(odd_ones_out([75, 68, 75, 47, 68]), [75, 68, 75, 68])
print(odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67]), [67, 67])
print(odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100]), [100, 100, 100, 100])
print(odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50]), [44, 79, 50, 44, 79, 50])