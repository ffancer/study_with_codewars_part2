def obfuscate(email):
    return email.replace('@', ' [at] ').replace('.', ' [dot] ')


print(obfuscate('test@123.com'), 'test [at] 123 [dot] com')
print(obfuscate('Code_warrior@foo.ac.uk'), 'Code_warrior [at] foo [dot] ac [dot] uk')
