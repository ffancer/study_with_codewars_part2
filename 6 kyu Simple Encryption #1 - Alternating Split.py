def decrypt(encrypted_text, n):
    if encrypted_text is None:
        return None

    encrypt_lenght = len(encrypted_text)
    second_chars = encrypted_text[:encrypt_lenght // 2]
    other_chars = encrypted_text[encrypt_lenght // 2:]

    if n <= 0:
        return encrypted_text
    else:
        for pos in range(len(other_chars)):
            encrypted_text += other_chars[pos] + second_chars[pos:pos + 1]
        return decrypt(encrypted_text[encrypt_lenght:], n - 1)


def encrypt(text, n):
    second_chars = ""
    other_chars = ""

    if n <= 0:
        return text
    else:
        for pos in range(len(text)):
            if pos % 2 != 0:
                second_chars += text[pos]
            else:
                other_chars += text[pos]
        return encrypt(second_chars + other_chars, n - 1)


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
