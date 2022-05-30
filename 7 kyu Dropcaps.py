def drop_cap(str_):
    s = str_.split(' ')
    lst = []
    for i in s:
        if len(i) > 2:
            lst.append(i.title())
        else:
            lst.append(i)
    return ' '.join(lst)


print(drop_cap('Apple Banana'), "Apple Banana")
print(drop_cap('Apple'), "Apple")
print(drop_cap(''), "")
print(drop_cap("   space WALK   "), "   Space Walk   ")
