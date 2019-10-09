def evenNumbersBeforeFixed(sequence, fixedElement):
    ctr = 0
    
    for i in sequence:
        
        if i == fixedElement:
            return ctr
        if i % 2 == 0:
            ctr += 1
    return -1

