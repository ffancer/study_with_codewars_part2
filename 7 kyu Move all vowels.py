def move_vowels(input):
    five_vowels = 'aeiou'
    not_vowels, vowels = '', ''

    for i in input:
        if i in five_vowels:
            vowels +=i
        else:
            not_vowels += i

    return not_vowels + vowels


print(move_vowels('day'), 'dya')
print(move_vowels('apple'), 'pplae')
print(move_vowels('peace'), 'pceae')
print(move_vowels('maker'), 'mkrae')
print(move_vowels('programming'), 'prgrmmngoai')
print(move_vowels('javascript'), 'jvscrptaai')
print(move_vowels('python'), 'pythno')
print(move_vowels('ruby'), 'rbyu')
print(move_vowels('haskell'), 'hskllae')
print(move_vowels('clojure'), 'cljroue')
print(move_vowels('csharp'), 'cshrpa')
