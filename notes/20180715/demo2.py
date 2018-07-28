# coding:utf8
PI = 3.14


def count_sqr(r):
    if not isinstance(r, (int, float)):
        raise TypeError('bad operand type')
    s = PI * r * r
    return s


rs = [
    1,
    2.1,
    73.1,
]
for r0 in rs:
    s = count_sqr(r0)
    print(s)

abs(1)


def get_xy(r):
    x = r + 1
    y = r - 1
    return x, y


x, y = get_xy(100)
print(x, y)


def power(x, n=2, y=10, z=9):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(10))
print(power(10, 3))
print(power(10, n=3))


def calc(*numbers):
    print(numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4, 5, 6, 7, 8))
_l = [1, 2, 3, 4, 5, 6, 7, 8]
print(calc(*_l))


def person(name, age, **kw):
    import pdb
    pdb.set_trace()
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Michael', 30))
print(person('Adam', 45, gender='M', job='Engineer', aaa='bbb'))


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)


def fact(n):
    print(n)
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact_(n):
    t = 1
    while n != 1:
        t = t * (n)
        n -= 1
    return t


fact(3)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-3:])
print(L[-2:-1])


L = list(range(100))

print('*'*100)
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


for k in d.values():
    print(k)

for k, v in d.items():
    print(k, v)

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

print([x * x for x in range(1, 11) if x > 5])

print([m + n for m in 'ABC' for n in 'XYZ'])

L = []
for m in 'ABC':
    for n in 'XYZ':
        L.append(m+n)
print(L)

import os
print([d for d in os.listdir('.')])

g = (x * x for x in range(100000))
print(g)

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


g = fib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


aa = map(char2num, '13579')
print(aa)
# print(list(aa))
print(reduce(fn, aa))

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


fn = lambda x, y: x * 10 + y


def fn1(x, y):
    return x * 10 + y


def str2int(s):
    return reduce(fn, map(char2num, s))
print(str2int('12345'))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


sorted([36, 5, -12, 9, -21], key=my_abs)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

f = lambda n: n % 2 == 1
L = list(filter(f, range(1, 20)))


def log(func):
    def wrapper(*args, **kw):
        import time
        t0 = time.time()
        print('begin call %s():' % func.__name__)
        f = func(*args, **kw)
        print('finish call %s():' % func.__name__)
        print('t_diff:{}'.format(time.time() - t0))
        return f

    return wrapper


@log
def now():
    print('2015-3-25')


@log
def now1():
    print('2015-3-26')


@log
def now2():
    print('2015-3-27')


now()
now1()
now2()


def my_log(a, b, c):
    print(a, b, c)


import functools

my_log1 = functools.partial(my_log, 1, 2)

my_log(1, 2, 3)
my_log(1, 2, 1)
my_log(1, 2, 2)
my_log1(4)

