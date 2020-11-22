a = int(input('Первое число'))
b = int(input('Второе число'))
if b > a:
    m = a
    a = b
    b = m
r = a % b
while(r != 0):
    a = b
    b = r
    q = a / b
    r = a - (q * b)
gcd = b
print(gcd)