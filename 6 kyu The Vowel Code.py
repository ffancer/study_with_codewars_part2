def encode(st):
    return st.replace('a', '1').replace('e', '2').replace('i', '3').replace('o', '4').replace('u', '5')


def decode(st):
    return st.replace('1', 'a').replace('2', 'e').replace('3', 'i').replace('4', 'o').replace('5', 'u')


print(encode('hello'), 'h2ll4')
print(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
print(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
print(decode('h2ll4'), 'hello')
