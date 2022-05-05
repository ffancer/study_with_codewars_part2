# CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    lst = []

    for i in string:
        lst.append(CHAR_TO_MORSE.get(i, i))

    return ' '.join(lst)


print(encryption("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
print(encryption("SOS"), "... --- ...")
print(encryption("1836"), ".---- ---.. ...-- -....")
print(encryption("THE QUICK BROWN FOX"), "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-")
print(encryption("JUMPED OVER THE"), ".--- ..- -- .--. . -..   --- ...- . .-.   - .... .")
