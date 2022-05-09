def pass_the_door_man(word):
    a = 0

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            a = word[i]

    return (ord(a) - 96) * 3


print(pass_the_door_man("lettuce"), 60)
print(pass_the_door_man("hill"), 36)
print(pass_the_door_man("apple"), 48)
