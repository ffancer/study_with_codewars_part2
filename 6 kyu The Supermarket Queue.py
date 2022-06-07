def queue_time(customers, n):
    lst = [0]*n

    for i in customers:
        lst = sorted(lst)
        lst[0] += i

    return max(lst)


print(queue_time([], 1), 0, "wrong answer for case with an empty queue")
print(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
print(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
print(queue_time([1, 2, 3, 4, 5], 1), 15, "wrong answer for a single till")
print(queue_time([1, 2, 3, 4, 5], 100), 5, "wrong answer for a case with a large number of tills")
print(queue_time([2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")
