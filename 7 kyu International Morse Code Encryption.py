# CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    for i in CHAR_TO_MORSE.values():
        print(i)


print(encryption("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
print(encryption("SOS"), "... --- ...")
print(encryption("1836"), ".---- ---.. ...-- -....")
print(encryption("THE QUICK BROWN FOX"), "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-")
print(encryption("JUMPED OVER THE"), ".--- ..- -- .--. . -..   --- ...- . .-.   - .... .")
