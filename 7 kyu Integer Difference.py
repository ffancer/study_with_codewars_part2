def int_diff(lst, n):
    cnt = 0
    i,j=0,1

    while j < len(lst)-1:
        if abs(lst[i] - lst[j]) == n:
            cnt += 1
            i += 1
        j += 1
    return cnt

print(int_diff([1, 1, 5, 6, 9, 16, 27], 4), 3)
print(int_diff([1, 1, 3, 3], 2), 4)
