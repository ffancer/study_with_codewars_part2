# 7 kyu
# Thinkful - List and Loop Drills: Lists of lists

# from math import
def process_data(data):

    def diffr(items):
        return items[0] - sum(items[1:])

    for i in data:
        print(diffr(i))


print(process_data([[2, 5], [3, 4], [8, 7]]), 3)
print(process_data([[2, 9], [2, 4], [7, 5]]), 28)