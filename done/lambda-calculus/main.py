# Alonzo Church

true = lambda x: lambda y: x
false = lambda x: lambda y: y

ite = lambda b: lambda x: lambda y: b(x)(y)

not_ = lambda b: b(false)(true)
and_ = lambda x: lambda y: x(y)(false)
or_ = lambda x: lambda y: x(true)(y)
xor_ = lambda x: lambda y: x(not_(y))(y)
nand_ = lambda x: lambda y: not_(and_(x)(y))
nor_ = lambda x: lambda y: not_(or_(x)(y))

implies = lambda x: lambda y: x(y)(true)
equal = lambda x: lambda y: and_(x(y)(not_(y)))(y(x)(not_(x)))
add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

zero = lambda f: lambda x: x 
one = lambda f: lambda x: f(x) 
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))

to_int = lambda n: n(lambda x: x+1)(0)

succ = lambda n: lambda f: lambda x: f(n(f)(x))

pair = lambda a: lambda b: lambda f: f(a)(b)
first = lambda p: p(lambda a: lambda b: a)
second = lambda p: p(lambda a: lambda b: b)

step = lambda p: pair(succ(first(p)))(first(p))
pred = lambda n: second(n(step)(pair(zero)(zero)))

sub = lambda m: lambda n: n(pred)(m)
is_zero = lambda n: n(lambda _: false)(true)


print(to_int(add(two)(three)))
print(to_int(succ(two)))
print(to_int(pred(three)))