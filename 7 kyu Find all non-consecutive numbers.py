def all_non_consecutive(arr):
    answer = []

    for i in range(len(arr)-1):
        if arr[i + 1] - arr[i] != 1:
            answer.append({'i': i + 1, 'n': arr[i + 1]})

    return answer


print(all_non_consecutive([1, 2, 3, 4, 6, 7, 8, 10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])
