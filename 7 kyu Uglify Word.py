def uglify_word(s):
    return


print(uglify_word("AAA"), "AaA")
print(uglify_word("AaA"), "AaA")
print(uglify_word("BbB"), "BbB")
print(uglify_word("aaa-bbb-ccc"), "AaA-BbB-CcC")
print(uglify_word("AaA-BbB-CcC"), "AaA-BbB-CcC")
print(uglify_word("eeee-ffff-gggg"), "EeEe-FfFf-GgGg")
print(uglify_word("EeEe-FfFf-GgGg"), "EeEe-FfFf-GgGg")
print(uglify_word("qwe123asdf456zxc"), "QwE123AsDf456ZxC")
print(uglify_word("Hello World"), "HeLlO WoRlD")
