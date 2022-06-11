def triple_double(num1, num2):
    triple = ''
    num1, num2 = str(num1), str(num2)

    for i in range(len(num1)-2):
        if num1[i] == num1[i+1] == num1[i+2]:
            triple += num1[i] + num1[i+1] + num1[i+2]

    while num2:
        if triple == num2[:3]:
            return 1
        num2 = num2[3::]
    # return 0


print(triple_double(451999277, 41177722899), 1)
print(triple_double(1222345, 12345), 0)
print(triple_double(12345, 12345), 0)
print(triple_double(666789, 12345667), 1)
print(triple_double(10560002, 100), 1)
print(triple_double(1112, 122), 0)
