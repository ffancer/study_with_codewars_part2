# 7 kyu
# Thinkful - List and Loop Drills: Lists of lists


def process_data(data):
    result = 1
    for item in data:
        result *= item[0] - item[1]
    return result


print(process_data([[2, 5], [3, 4], [8, 7]]), 3)
print(process_data([[2, 9], [2, 4], [7, 5]]), 28)
