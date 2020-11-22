def gcd(a, b):
    if b > a:
        m = a
        a = b
        b = m
    r = a % b
    while(r != 0):
        a = b
        b = r
        q = a // b
        r = a - (q * b)
    return b
# Примеры    
print( gcd(180, 150) )
print( gcd(98, 5) )
