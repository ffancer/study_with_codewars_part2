def to_camel_case(text):
    if '-' in text:
        text = text.split('-')
        if text[0][0].islower():

        return ''.join(text)
    elif '_' in text:
        text = text.split('_')
        return ''.join(text)
    return ''


print(to_camel_case(''), '', "An empty string was provided but not returned")
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
      "to_camel_case('the_stealth_warrior') did not return correct value")
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
      "to_camel_case('The-Stealth-Warrior') did not return correct value")
print(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
