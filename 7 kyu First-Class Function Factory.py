def factory(x):
    def some(array):
        new = []
        for i in array:
            new.append(i * x)
        return new

    return some


my_arr = [1, 2, 3]

threes = factory(3)
print(threes(my_arr), [3, 6, 9])

fives = factory(5)
print(fives(my_arr), [5, 10, 15])
