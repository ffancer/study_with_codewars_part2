from math import pi


def find(array, element):
    # if element in array:
    #     return array.index(element)
    # return 'Not found'
    return array.index(element) if element in array else 'Not found'

array = [2, 3, 5, 7, 11]
print(find(array, 5), 2)
print(find(array, 11), 4)
print(find(array, 3), 1)
print(find(array, 2), 0)
print(find(array, 7), 3)
print(find(array, 1), 'Not found')
print(find(array, 8), 'Not found')

array = [True, 'Hello World', False, 'Lorem Ipsum', 6, pi]
print(find(array, 'Hello World'), 1)
print(find(array, 'lorem ipsum'), 'Not found')
print(find(array, 'Lorem Ipsum'), 3)
print(find(array, False), 2)
print(find(array, True), 0)
print(find(array, pi), 5)
print(find(array, 3.14), 'Not found')
print(find(array, 6), 4)
