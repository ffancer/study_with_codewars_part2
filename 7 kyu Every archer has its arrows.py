def archers_ready(archers):
    pass


print(archers_ready([]), False, "Should handle no archers")
print(archers_ready([1, 2, 3, 4]), False, "Should handle unprepared archers")
print(archers_ready([5, 6, 7, 8]), True, "Should handle prepared archers")
