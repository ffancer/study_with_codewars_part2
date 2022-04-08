def compose(s1, s2):
    s1, s2 = s1.split('\n'), s2.split('\n')
    ans = ''

    ans += s1[0][0] + s2[3][0:] + ' '
    ans += s1[1][0] + s2[2][0:] + ' '
    ans += s1[2][0] + s2[1][0:] + ' '
    ans += s1[3][0] + s2[0][0:] + ' '

    return ans.replace(' ', '\n')[:-1]


print(compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"),
      "bNkTB\nhTrWO\nRTFVi\nCnnIj")
print(compose("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"),
      "HgYPW\nTGGbM\nIPhqt\nuUMDH")
