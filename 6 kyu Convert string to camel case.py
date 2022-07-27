def to_camel_case(text):
    if '-' in text:
        text = text.split('-')
        if text[0][0].islower():
            return ''.join(i.title for i in text)
        return ''.join(text)
    elif '_' in text:
        text = text.split('_')
        return ''.join(text)
    return ''


print(to_camel_case(''), '')
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
print(to_camel_case("A-B-C"), "ABC")
