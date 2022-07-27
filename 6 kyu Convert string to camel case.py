def to_camel_case(text):
    if '_' in text:
        text = text.replace('_', '-')
    if '-' in text:
        text = text.split('-')
        if text[0][0].islower():
            return text[0] + ''.join(i.title() for i in text[1:])
        elif text[0][0].isupper():
            return ''.join(i.title() for i in text)
    return ''


print(to_camel_case(''), '')
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
print(to_camel_case("The-stealth-warrior"), "TheStealthWarrior")
print(to_camel_case("A-B-C"), "ABC")
