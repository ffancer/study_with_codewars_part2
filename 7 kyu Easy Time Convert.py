def time_convert(num):
    # if num <= 0:
    #     return '00:00'
    #
    # minute = num % 60
    #
    # return f'00:{minute}'
    return num * 60 // 3600


print(time_convert(0), '00:00', 'Test at 0')
print(time_convert(-6), '00:00', 'Negative number')
print(time_convert(8), '00:08', '8 minutes')
print(time_convert(32), '00:32', '32 minutes')
print(time_convert(75), '01:15', 'over an hour')
print(time_convert(63), '01:03', 'over an hour')
print(time_convert(134), '02:14', 'over two hours')
print(time_convert(180), '03:00', 'three hours')
print(time_convert(970), '16:10', 'over 16 hours')
print(time_convert(565757), '9429:17', 'big numbers')
