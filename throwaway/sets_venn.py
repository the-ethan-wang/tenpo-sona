def is_prime(n: int): # No point in optimising, n<=100
    if(n<=1):
        return False
    if n==2:
        return True
    for i in range(2, n//2+1):
        if(n%i==0):
            return False
    return True

for i in range(101):
    if(is_prime(i)):
        print(i)


import math

print(math.log(100, math.e))

count=0
for i in range(1, 101):
    if(i%4==1 or is_prime(i)):
        count+=1

print(count)

digs = [2, 5, 7, 8]
a = set()
for i in range(4):
    for j in range(4):
        for k in range(4):
            if(i!=j and j!=k):
                a.add(int("".join([str(x) for x in [digs[i], digs[j], digs[k]]])))

a = sorted(list(a))

print(len([x for x in a if int(x)%13==0]))
print(len([x for x in a if is_prime(int(x))]))

def get_hprob_below_half(n):
    # n is odd int >=3
    numerator=0
    for mask in range(1<<n):
        hcount=0
        for i in range(n):
            if((mask>>i)&1):
                hcount+=1

        if(hcount<=(n//2)):
            numerator+=1
    denominator = (1<<n)
    return(numerator, denominator)

for i in range(3, 11, 2):
    print(get_hprob_below_half(i))

def merge_sorted(a, b):
    c=[]
    i=0
    j=0
    while(i<len(a)and j<len(b)):
        if(a[i]<=b[j]):
            i+=1
            c.append(a[i])
        else:
            j+=1
            c.append(b[i])
    for k in range(i, len(a)):
        c.append(a[k])
    for k in range(j, len(b)):
        c.append(b[k])
    return c

def is_subset(a, b):
    return any([1 for item in a if item not in b])

def get_inter(a, b):
    c = set(a).intersection(set(b))
    return c

for i in {1, 2, 5}:
    print(i)

print(len(set("algebra")))

print(len([i for i in range(1, 100) if i%7==0]))

import random

sample0 = [random.random() for i in range(1000)]

sample1=[min(random.random(), random.random()) for i in range(1000)]

sample2=[random.random()**2 for i in range(1000)]

def mean(a):
    return sum(a)/len(a)

def median(a):
    assert a!=[]
    return sorted(a)[len(a)//2]

import numpy as np
import pandas as pd

data = {
    "": ["Sample 0", "Sample 1", "Sample 2"],
    "mean": [mean(sample0), mean(sample1), mean(sample2)],
    "median": [median(sample0), median(sample1), median(sample2)],
}

bleh = pd.DataFrame(data=data)

print(bleh)

from itertools import combinations, permutations, combinations_with_replacement

# hmmmm
# print([x for x in combinations_with_replacement(permutations(combinations([*range(6)], 5), 5), 5)])
# lost sys.stderr moment (im a ctrl+C user)

""" btw wtf is ValuesAsNumpy like um ok"""