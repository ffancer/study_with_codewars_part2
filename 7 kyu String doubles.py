def doubles(s):
    lst = []
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lst.append(s[:i+1])
    return list(s)

print(doubles('abbbzz'), 'ab')
print(doubles('zzzzykkkd'), 'ykd')
print(doubles('abbcccdddda'), 'aca')
print(doubles('vvvvvoiiiiin'), 'voin')
print(doubles('rrrmooomqqqqj'), 'rmomj')
print(doubles('xxbnnnnnyaaaaam'), 'bnyam')
