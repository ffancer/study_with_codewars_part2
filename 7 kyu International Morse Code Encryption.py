# CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    s = ''
    for i in string:
        if i in CHAR_TO_MORSE.keys():
            s += CHAR_TO_MORSE[i] + ' '
        if i == ' ':
            s += '  '
    return s[:-1]


print(encryption("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
print(encryption("SOS"), "... --- ...")
print(encryption("1836"), ".---- ---.. ...-- -....")
print(encryption("THE QUICK BROWN FOX"), "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-")
print(encryption("JUMPED OVER THE"), ".--- ..- -- .--. . -..   --- ...- . .-.   - .... .")
