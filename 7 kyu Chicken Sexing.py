def correctness(bobs_decisions, expert_decisions):
    cnt = 0
    for i in bobs_decisions:
        for j in expert_decisions:
            # if i == j:
            #     cnt += 1
            print(j)
    return cnt

print(correctness(('M', 'F', '?'), ('M', 'F', '?')), 3)
print(correctness(('M', '?', 'M'), ('M', 'F', '?')), 2)
print(correctness(('F', 'M', 'F'), ('M', 'F', 'M')), 0)
