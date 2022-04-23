def add(a):
    def add_b(b):
        return a + b
    return add_b


print(callable(add(32)), "The first call did not return a function")
print(callable(add(15)), "The first call did not return a function")
