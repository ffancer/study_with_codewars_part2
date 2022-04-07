# 7 kyu
# Ce*s*r*d Strings


def uncensor(infected, discovered):
    discovered_iter = iter(discovered)
    return ''.join(next(discovered_iter) if i == '*' else i for i in discovered_iter)


print(uncensor('*h*s *s v*ry *tr*ng*', 'Tiiesae'), 'This is very strange')
print(uncensor('A**Z*N*', 'MAIG'), 'AMAZING')
print(uncensor('xyz', ''), 'xyz')
print(uncensor('', ''), '')
print(uncensor('***', 'abc'), 'abc')
