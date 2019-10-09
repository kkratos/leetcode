def higherVersion(ver1, ver2):
    x1 = ver1.split('.')
    x2 = ver2.split('.')
    
    for i in range(len(x1)):
        y1 = int(x1[i])
        y2 = int(x2[i])
        
        if y1 == y2:
            continue
        if y1 > y2:
            return True
        if y1 < y2:
            return False
    return False