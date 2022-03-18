def nth_char(words):
    s = ''

    for i,j in enumerate(words):
        s += j[i]

    return s


print(nth_char(['yoda', 'best', 'has']), 'yes')
print(nth_char([]), '')
print(nth_char(['X-ray']), 'X')
print(nth_char(['No', 'No']), 'No')
print(nth_char(['Chad', 'Morocco', 'India', 'Algeria', 'Botswana', 'Bahamas', 'Ecuador', 'Micronesia']),
      'Codewars')
