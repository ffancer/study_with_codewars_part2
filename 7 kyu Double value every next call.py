class Class:
    value = 0

    @staticmethod
    def get_number():
        if Class.value == 0:
            Class.value = 1
            return 1
        else:
            Class.value *= 2
            return Class.value


print(Class.get_number(),  1, "1st call should return 1")
print(Class.get_number(),  2, "2nd call should return 2")
print(Class.get_number(),  4, "3rd call should return 4")
print(Class.get_number(),  8, "4th call should return 8")
print(Class.get_number(), 16, "5th call should return 16")
