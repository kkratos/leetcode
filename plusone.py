def plusone(digits):
    rev = 0
    for i in digits:
        rev = rev * 10 + i
    rev += 1
    return rev
    s = str(rev)

    return list(map(int, list(s)))

a = [1, 2, 3]
print(plusone(a))