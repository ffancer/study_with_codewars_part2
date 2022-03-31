def spacey(array):
    i = 1
    lst = [array[0]]

    while len(array) != len(lst):
        first = ''.join(array[:i+1])
        lst.append(first)
        i += 1
    return lst


print(spacey(['kevin', 'has', 'no', 'space']), ['kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
print(spacey(['this', 'cheese', 'has', 'no', 'holes']),
                   ['this', 'thischeese', 'thischeesehas', 'thischeesehasno', 'thischeesehasnoholes'])
