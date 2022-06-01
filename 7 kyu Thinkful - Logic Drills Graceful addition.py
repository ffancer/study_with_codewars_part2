# 7 kyu
# Thinkful - Logic Drills: Graceful addition


def my_add(a, b):
    try:
        return a + b
    except:
        return None


print(my_add(1, 3.414), 4.414)
print(my_add(42, " is the answer."), None)
print(my_add(10, "2"), None)
