def convert(number):
    lst, i = [], 0

    while i < len(number):
        lst.append(number[i: i + 2])
        i += 2

    lst = [int(i) for i in lst]

    return lst

print(convert("65"), "A")
print(convert("656667"), "ABC")
print(convert("676584"), "CAT")
print(convert("73327673756932858080698267658369"), "I LIKE UPPERCASE")
