# 7 kyu
# Ce*s*r*d Strings


def uncensor(infected, discovered):
    s = ''
    a = iter(discovered)
    s += str(a)
    return s


print(uncensor('*h*s *s v*ry *tr*ng*', 'Tiiesae'), 'This is very strange')
print(uncensor('A**Z*N*', 'MAIG'), 'AMAZING')
print(uncensor('xyz', ''), 'xyz')
print(uncensor('', ''), '')
print(uncensor('***', 'abc'), 'abc')
