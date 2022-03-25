# 7 kyu
# Can Santa save Christmas?


def determine_time(arr):
    total, hours, minutes, seconds = 0, 0, 0, 0

    for i in arr:
        hours += int(i.split(':')[0])
        minutes += int(i.split(':')[1])
        seconds += int(i.split(':')[2])

    total = hours * 3600 + minutes * 60 + seconds

    return total <= 24 * 3600


print(determine_time(["01:00:00", "02:30:00"]), True)
print(determine_time(["01:00:00", "02:30:00", "22:00:00"]), False)
print(determine_time(["12:00:00", "12:00:00"]), True)
print(determine_time([]), True)
