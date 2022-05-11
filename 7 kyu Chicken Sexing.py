def correctness(bobs_decisions, expert_decisions):
    cnt = 0

    for i in range(len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            cnt += 1
        if (bobs_decisions[i] != expert_decisions[i]) and (bobs_decisions[i] == '?' or expert_decisions[i] == '?'):
            cnt += .5

    return cnt


print(correctness(('M', 'F', '?'), ('M', 'F', '?')), 3)
print(correctness(('M', '?', 'M'), ('M', 'F', '?')), 2)
print(correctness(('F', 'M', 'F'), ('M', 'F', 'M')), 0)
