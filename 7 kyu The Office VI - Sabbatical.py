def sabb(s, val, happiness):
    word = 'sabbatical'
    cnt = 0

    for i in word:
        if i in s:
            cnt += 1

    return "Sabbatical! Boom!" if cnt + val + happiness > 22 else "Back to your desk, boy."


print(sabb("Can I have a sabbatical?", 5, 5), "Sabbatical! Boom!")
print(sabb("Why are you shouting?", 7, 2), "Back to your desk, boy.")
print(sabb("What do you mean I cant learn to code??", 8, 9), "Sabbatical! Boom!")
print(sabb("Please calm down", 9, 1), "Back to your desk, boy.")
