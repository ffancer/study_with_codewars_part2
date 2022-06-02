def title_to_number(title):
    total = 0
    # return ord('A') - 64
    # for i in range(len(title)):
    for j in title:
        total += ord(j) - 64

    return total


print(title_to_number('A'), 1)
print(title_to_number('Z'), 26)
print(title_to_number('AA'), 27)
print(title_to_number('AZ'), 52)
print(title_to_number('BA'), 53)
