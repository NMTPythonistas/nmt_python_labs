from math import *

def evaluate_at(x, a=2, max_k=1000):
    return sum([sin(pi * k ** a * x) / (pi * k ** a)
                for k in range(1, max_k + 1)])
