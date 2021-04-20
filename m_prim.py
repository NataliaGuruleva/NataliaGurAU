import math
def wilson_test(n):
    if (math.factorial(n - 1) + 1) % n == 0:
        return True
    else:
        return False