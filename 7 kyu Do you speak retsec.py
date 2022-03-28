# 7 kyu
# Do you speak retsec?


def reverse_by_center(s):
    if len(s) % 2 == 0:
        return s[:len(s)//2], s[len(s)//2:]


print(reverse_by_center("secret"), "retsec")
print(reverse_by_center("agent"), "nteag")
print(reverse_by_center("raw"), "war")
print(reverse_by_center("onion"), "onion")
