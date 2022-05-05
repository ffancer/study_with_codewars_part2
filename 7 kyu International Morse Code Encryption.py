# CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    s = ''
    for i in string.split():
        if i in CHAR_TO_MORSE.values():
            s += CHAR_TO_MORSE[i]
    return s


print(encryption("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
print(encryption("SOS"), "... --- ...")
print(encryption("1836"), ".---- ---.. ...-- -....")
print(encryption("THE QUICK BROWN FOX"), "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-")
print(encryption("JUMPED OVER THE"), ".--- ..- -- .--. . -..   --- ...- . .-.   - .... .")
