def egcd(a, b):
    x = 1
    y = 0
    x1 = 0
    y1 = 1
    while a != 0 and b != 0:
        q = a // b
        r = a - (b * q)
        c = x - (x1 * q)
        d = y - (y1 * q)
        a = b
        b = r
        x = x1
        y = y1
        x1 = c
        y1 = d
    gcd = b
    return(gcd, x, y)
# Пример    
print( egcd(98, 5) )
    




