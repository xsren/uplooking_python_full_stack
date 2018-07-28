# coding:utf8

def test():
    print('aaa')


print(u'包含中文的str')
print(ord('A'))
print(ord(u'中'))
print(chr(66))

# python3使用这个函数
# print(chr(25991))
# python2使用这个函数
# print(unichr(25991))
aaa = u'中文'
bbb = aaa.encode('utf8')
ccc = bbb.decode('utf8')
print(aaa)

test()
print(aaa)
x = b'ABC'
print(x)

print(len('ABC'))
print(len(u'中文'))
print(len(b'ABC'))
print(len(u'中文'.encode('utf-8')))

name = u'小明'
score = 17.125
print(u'Hello, {0}, 成绩提升了 {1:.1f}%'.format(name, score))
print(u'Hello, {0}, 成绩提升了 {1}%'.format(name, score))

classmates = [
    'Michael',
    'Bob',
    'Tracy'
]

import pdb

pdb.set_trace()
print(len(classmates))
print(classmates[0])
# print(classmates[3])
print(classmates[-1])
classmates.append('Adam')
classmates.insert(1, 'Jack')
name = classmates.pop()
classmates.pop(1)
classmates[1] = 'Sarah'
L = ['Apple', 123, True]

for name in classmates:
    print(name)

for x in range(5):
    print(x)

sum = 0

for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99

while n > 0:
    sum = sum + n
    n = n - 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        print(n)
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    if n < 30:
        break
print(sum, n)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
import pdb

pdb.set_trace()
d['Adam'] = 67

d['Jack'] = 90
d['Jack'] = 88
print('Thomas' in d)
d.get('Thomas', -1)
d.get('Thomas')
d['Thomas']
d.pop('Bob')

s = set([1, 2, 3])
_l = [1, 1, 2, 3, 3]
new_l = list(set(_l))
print(s, _l, new_l)
s.add(4)
print(s)
s.remove(4)
print(s)
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)
a = 'abcaaa'
b = a.replace('a', 'A')
print(a, b)
