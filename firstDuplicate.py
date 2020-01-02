def firstDuplicate(s):
    a = set()
    for i in s:
        if i in a:
            return i
        a.add(i)
    return -1

s = [2, 1, 3, 4, 3, 2]
print(firstDuplicate(s))