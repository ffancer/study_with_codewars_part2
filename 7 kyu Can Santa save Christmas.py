def determine_time(arr):
    pass


print(determine_time(["01:00:00", "02:30:00"]), True)
print(determine_time(["01:00:00", "02:30:00", "22:00:00"]), False)
print(determine_time(["12:00:00", "12:00:00"]), True)
print(determine_time([]), True)
