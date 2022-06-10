def encode(st):
    return st.translate(str.maketrans('aeiou', '12345'))


def decode(st):
    return st.translate(str.maketrans('12345', 'aeiou'))


print(encode('hello'), 'h2ll4')
print(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
print(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
print(decode('h2ll4'), 'hello')
