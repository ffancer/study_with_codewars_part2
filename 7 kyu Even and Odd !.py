def even_and_odd(n):
    even, odd = '', ''

    for i in str(n):
        if int(i) % 2 == 0:
            even += i
        else:
            odd += i

    if even == '':
        even = '0'
    elif odd == '':
        odd = '0'

    return int(even), int(odd)


print(even_and_odd(126453), (264, 153))
print(even_and_odd(3012), (2, 31))
print(even_and_odd(4628), (4628, 0))

