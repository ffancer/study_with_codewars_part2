def triple_double(num1, num2):
    num1, num2 = str(num1), str(num2)

    for i in num1:
        if i * 3 in num1 and i * 2 in num2:
            return 1
    return 0


print(triple_double(451999277, 41177722899), 1)
print(triple_double(1222345, 12345), 0)
print(triple_double(12345, 12345), 0)
print(triple_double(666789, 12345667), 1)
print(triple_double(10560002, 100), 1)
print(triple_double(1112, 122), 0)
