def title_to_number(title):
    return ord('A') - 64


print(title_to_number('A'), 1)
print(title_to_number('Z'), 26)
print(title_to_number('AA'), 27)
print(title_to_number('AZ'), 52)
print(title_to_number('BA'), 53)
