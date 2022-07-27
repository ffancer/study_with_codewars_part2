def to_camel_case(text):
    pass


print(to_camel_case(''), '', "An empty string was provided but not returned")
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
      "to_camel_case('the_stealth_warrior') did not return correct value")
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
      "to_camel_case('The-Stealth-Warrior') did not return correct value")
print(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
