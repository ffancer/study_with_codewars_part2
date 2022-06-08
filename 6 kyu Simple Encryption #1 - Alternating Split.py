def decrypt(encrypted_text, n):
    pass


def encrypt(text, n):
    pass


print(encrypt("This is a test!", 0), "This is a test!")
print(encrypt("This is a test!", 1), "hsi  etTi sats!")
print(encrypt("This is a test!", 2), "s eT ashi tist!")
print(encrypt("This is a test!", 3), " Tah itse sits!")
print(encrypt("This is a test!", 4), "This is a test!")
print(encrypt("This is a test!", -1), "This is a test!")
print(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

print(decrypt("This is a test!", 0), "This is a test!")
print(decrypt("hsi  etTi sats!", 1), "This is a test!")
print(decrypt("s eT ashi tist!", 2), "This is a test!")
print(decrypt(" Tah itse sits!", 3), "This is a test!")
print(decrypt("This is a test!", 4), "This is a test!")
print(decrypt("This is a test!", -1), "This is a test!")
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

print(encrypt("", 0), "")
print(decrypt("", 0), "")
print(encrypt(None, 0), None)
print(decrypt(None, 0), None)
