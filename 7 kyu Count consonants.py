def consonant_count(s):
    return sum(1 for i in s.lower() if i not in 'aeiou' and i.isalpha())


print(consonant_count(''), 0, 'Test string is empty string')
print(consonant_count('aaaaa'), 0, 'Test string: "aaaaa"')
print(consonant_count('XaeiouX'), 2, 'Test string: "XaeiouX"')
print(consonant_count('Bbbbb'), 5, 'Test string: "Bbbbb"')
print(consonant_count('helLo world'), 7, 'Test string: "helLo world"')
print(consonant_count('h^$&^#$&^elLo world'), 7, 'Test string: "h^$&^#$&^elLo world"')
print(consonant_count('0123456789'), 0, 'Test string: "0123456789"')
print(consonant_count('012345_Cb'), 2, 'Test string: "012345_Cb"')
