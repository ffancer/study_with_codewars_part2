def strong_enough(earthquake, age):
    total = 1

    for i in earthquake:
        total *= sum(i)

    return "Safe!" if total <= 1000 * 0.99 ** age else "Needs Reinforcement!"


print(strong_enough([[2, 3, 1], [3, 1, 1], [1, 1, 2]], 2), "Safe!")
print(strong_enough([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 2), "Safe!")
print(strong_enough([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 3), "Needs Reinforcement!")
