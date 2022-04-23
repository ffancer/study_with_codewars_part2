def am_I_afraid(day, num):
    dct = {'Monday': 12, 'Tuesday': num > 95, 'Wednesday': 34, 'Thursday': 0,
           'Friday': num % 2 == 0, 'Saturday': 56, 'Sunday': abs(num) == 666}


print(am_I_afraid("Monday", 13), False, 'Should return false')
print(am_I_afraid("Sunday", -666), True, 'Should return true')
print(am_I_afraid("Tuesday", 2), False, 'Should return false')
print(am_I_afraid("Tuesday", 965), True, 'Should return true')
print(am_I_afraid("Friday", 2), True, 'Should return true')
