def uglify_word(s):
    s_lower, s_upper = s.lower(), s.upper()
    lst = []
    if s == s.lower() and '-' in s:
        s = s.split('-')
        for i in s:
            for j in range(len(i)):
                if j % 2 == 0:
                    lst.append(i[j].upper())
                else:
                    lst.append(i[j].lower())
    return lst

print(uglify_word("AAA"), "AaA")
print(uglify_word("AaA"), "AaA")
print(uglify_word("BbB"), "BbB")
print(uglify_word("aaa-bbb-ccc"), "AaA-BbB-CcC")
print(uglify_word("AaA-BbB-CcC"), "AaA-BbB-CcC")
print(uglify_word("eeee-ffff-gggg"), "EeEe-FfFf-GgGg")
print(uglify_word("EeEe-FfFf-GgGg"), "EeEe-FfFf-GgGg")
print(uglify_word("qwe123asdf456zxc"), "QwE123AsDf456ZxC")
print(uglify_word("Hello World"), "HeLlO WoRlD")
