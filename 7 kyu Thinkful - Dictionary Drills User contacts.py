# 7 kyu
# Thinkful - Dictionary Drills: User contacts


def user_contacts(data):
    return {i[0]: (i[1] if len(i) == 2 else None) for i in data}


data = [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
expected_result = {'Grae Drake': 98110, 'Darrell Silver': 11201, 'Alex Nussbacher': 94101, 'Bethany Kok': None}
print(user_contacts(data), expected_result)
