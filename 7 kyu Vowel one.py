def vowel_one(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ''

    for i in s:
        if i in vowels:
            ans += '1'
        else:
            ans += '0'

    return ans


print(vowel_one("vowelOne"), "01010101")
print(vowel_one("123, arou"), "000001011")
print(vowel_one("Codewars"), "01010100")
print(vowel_one("Python"), "000010")