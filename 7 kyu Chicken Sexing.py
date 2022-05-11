def correctness(bobs_decisions, expert_decisions):
    # result=list(set(Ans) & set(Word))
    return len(sorted(list(set(bobs_decisions) & set(expert_decisions))))

print(correctness(('M', 'F', '?'), ('M', 'F', '?')), 3)
print(correctness(('M', '?', 'M'), ('M', 'F', '?')), 2)
print(correctness(('F', 'M', 'F'), ('M', 'F', 'M')), 0)
