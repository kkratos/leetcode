def commonCharacterCount(s1, s2):
    ctr = 0
    set1 = set(s1)
    for i in set1:
        s11 = s1.count(i)
        s22 = s2.count(i)
        ctr += min(s11, s22)
    return ctr
