def drop_cap(str_):
    return ' '.join(i.title() if len(i) > 2 else i for i in str_.split(' '))


print(drop_cap('Apple Banana'), "Apple Banana")
print(drop_cap('Apple'), "Apple")
print(drop_cap(''), "")
print(drop_cap("   space WALK   "), "   Space Walk   ")
