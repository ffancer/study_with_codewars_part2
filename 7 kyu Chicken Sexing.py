def correctness(bobs_decisions, expert_decisions):
    return [i for i in bobs_decisions if i in expert_decisions]

print(correctness(('M', 'F', '?'), ('M', 'F', '?')), 3)
print(correctness(('M', '?', 'M'), ('M', 'F', '?')), 2)
print(correctness(('F', 'M', 'F'), ('M', 'F', 'M')), 0)
