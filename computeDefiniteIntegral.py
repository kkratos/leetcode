def computeDefiniteIntegral(l, r, p):
    
    result = 0
    i = 0
    for c in p:
        i += 1
        result += (c * (r**i-l**i))/(i)
    
    return result
