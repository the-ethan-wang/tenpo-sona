import math

def get_val(b):
    assert 0<b<=1
    return (math.sin(b)-(1/math.asin(b)))

a = 0.9440390666
incr=0.00000000000001
while a+incr<=0.9440390667:
    a+=incr
    if(get_val(a)>0):
        print(get_val(a-incr), a-incr)
        print(get_val(a), a)
        break

# 0.944039066611608