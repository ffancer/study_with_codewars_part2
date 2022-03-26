def doubles(s):
    lst = []

    for i in s:
        if lst and lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)

    return ''.join(lst)


print(doubles('abbbzz'), 'ab')
print(doubles('zzzzykkkd'), 'ykd')
print(doubles('abbcccdddda'), 'aca')
print(doubles('vvvvvoiiiiin'), 'voin')
print(doubles('rrrmooomqqqqj'), 'rmomj')
print(doubles('xxbnnnnnyaaaaam'), 'bnyam')
