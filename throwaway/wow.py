import math

def get_val(b):
    assert 0<b<=1
    return (math.cos(b)-(1/math.acos(b)))

a =           0.4460476799991257
incr=         0.00000000000000001
while a+incr<=0.4460476799991258:
    print(a)
    a+=incr
    if(get_val(a)<0):
        print(get_val(a-incr), a-incr)
        print(get_val(a), a)
        break

# 4460476799991257