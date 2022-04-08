def compose(s1, s2):
    s1, s2 = s1.split('\n'), s2.split('\n')
    lst = []

    for n in range(len(s1)):
        append_1 = s1[n][:n + 1]
        append_2 = s2[-(n + 1)][:-n] if n > 0 else s2[-(n + 1)][:]
        lst.append(append_1 + append_2)

    return '\n'.join(lst)


print(compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"),
      "bNkTB\nhTrWO\nRTFVi\nCnnIj")
print(compose("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"),
      "HgYPW\nTGGbM\nIPhqt\nuUMDH")
