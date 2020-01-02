def specialPolynomial(x, n):
    sum = 0
    for i in range(1000):
        sum = sum  + x**i
        if sum > n:
            return i-1
    return 0
        
