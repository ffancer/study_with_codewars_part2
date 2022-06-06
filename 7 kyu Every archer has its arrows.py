def archers_ready(archers):
    if not archers:
        return False

    for i in archers:
        if i < 5:
            return False
    return True


print(archers_ready([]), False, "Should handle no archers")
print(archers_ready([1, 2, 3, 4]), False, "Should handle unprepared archers")
print(archers_ready([5, 6, 7, 8]), True, "Should handle prepared archers")
print(archers_ready([17, 15, 12, 7, 2, 12, 13, 15, 7, 11, 10, 5]), False)
