def obfuscate(email):
    lst = []

    for i in email:
        if i == '@':
            lst.append(' [at] ')
        elif i == '.':
            lst.append(' [dot] ')
        else:
            lst.append(i)

    return ''.join(lst)



print(obfuscate('test@123.com'), 'test [at] 123 [dot] com')
print(obfuscate('Code_warrior@foo.ac.uk'), 'Code_warrior [at] foo [dot] ac [dot] uk')
