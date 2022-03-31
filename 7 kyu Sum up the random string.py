def sum_from_string(strng):
    ans = 0
    s = ''

    for i in strng:
        if i.isdigit():
            s += i
        elif s:
            ans += int(s)
            s = ''

    if s:
        ans += int(s)

    return ans


print(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"), 2021)
print(sum_from_string("1+1=2"), 4)
print(sum_from_string("e=mc^2"), 2)
