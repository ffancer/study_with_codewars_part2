def spacey(array):
    # i = 0
    # first = array[i]
    # lst = []
    # while array:
    #     lst.append(first)
    #     first = array[0] + array[:i+1]
    #     i += 1
    # return lst
    return array[:1+1+1]


print(spacey(['kevin', 'has', 'no', 'space']), ['kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
print(spacey(['this', 'cheese', 'has', 'no', 'holes']),
                   ['this', 'thischeese', 'thischeesehas', 'thischeesehasno', 'thischeesehasnoholes'])
