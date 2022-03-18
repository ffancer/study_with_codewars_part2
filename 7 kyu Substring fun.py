def nth_char(words):
    for i,j in enumerate(words):
        print(i, j)


print(nth_char(['yoda', 'best', 'has']), 'yes')
print(nth_char([]), '')
print(nth_char(['X-ray']), 'X')
print(nth_char(['No', 'No']), 'No')
print(nth_char(['Chad', 'Morocco', 'India', 'Algeria', 'Botswana', 'Bahamas', 'Ecuador', 'Micronesia']),
      'Codewars')
