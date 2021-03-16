import random
import time
import sys
import multiprocessing
from multiprocessing import Pool

n = 100000
curr = 100

def calculate_pi(q):    
    count = 0
    for i in range(q):
        x=random.uniform(0, 1)
        y=random.uniform(0, 1)      
        if x * x + y * y <= 1:
            count = count + 1
    return count


def points(pool):
    l = pool.map(calculate_pi, [n]*curr)
    return l

if __name__=='__main__':
    pool = multiprocessing.Pool()
    N = sum(points(pool))
    pi = (N / (n * curr)) * 4
    t0 = time.time()
    print('пи:', pi)
    print("Time spent:", time.time() - t0)

