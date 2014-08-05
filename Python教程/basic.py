#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
In linux or Mac, execute "chmod a+x" hello.py to run py file immediately.
'''

# output
print 'hello, world'

print 'The quick brown fox', 'jumps over', 'the lazy dog'

print 300
print 100 + 200
print '100 + 200 = ', 100 + 200

# input
name = raw_input()
print name

name = raw_input('please enter your name: ')
print 'hello,', name

# print absolute value of an integer:
a = 100
if a >= 0:
  print a
else:
  print -a

# string 
print 'I\'m \"OK\"!'
print 'I\'m learning\n Python.'
print '\\\n\\'
print r'\\\t\\'
print '''line1
line2
line3'''

# boolean
print True and True
print True or False
print not False

# variable
a = 1
t_007 = 'T007'
Answer = True
a = 123
print a
a = 'ABC'
print a
b = a
a = 'XYZ'
print b

x = 10
x = x + 2

PI = 3.14159265369
print 10 / 3
print 10.0 / 3
print 10 % 3

# Unicode
'''
1. ASCII编码是1个字节，而Unicode编码通常是2个字节
2. ASCII编码实际上可以被看成是UTF-8编码的一部分
3. 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
'''

print ord('A')
print chr(65)

print u'中文'
print u'中'
print u'中文'.encode('utf-8')

print u'\u4e2d'
print u'ABC'.encode('utf-8')

print len(u'ABC')
print len('ABC')

print len(u'中文')

print len('\xe4\xb8\xad\xe6\x96\x87')

print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# format string output
print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%d.' % ('Michael', 100000)

print '%2d-%02d' % (3, 1)
print '%.2f' % 3.1415926
print 'Age: %s. Gender: %s' % (25, True)

print u'Hi, %s' % u'Michael'
print 'growth rate: %d %%' % 7
print u'中文'.encode('gb2312')

# list: sequential, changable
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0], classmates[1], classmates[2]
# print classmates[3]
print classmates[-1], classmates[-2], classmates[-3]
# print classmates[-4]

classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates

print classmates.pop()
print classmates

classmates[1] = 'Sarah'
print classmates

L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)
print s[2][1]
L = []
print len(L)

# tuple: sequential, unchangable
classmates = ('Michael', 'Bob', 'Tracy')
print classmates[0], classmates[-1]

t = (1, 2)
print t
t = ()
print t
t = (1)
print t
t = (1,)
print t
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t


# if
age = 20
if age >= 18:
  print 'your age is', age
  print 'adult'
else:
  print 'your age is', age
  print 'teenager'

if age >= 18:
  print 'adult'
elif age >= 6:
  print 'teenager'
else:
  print 'kid'

if age >= 6:
  print 'adult'
elif age >= 18:
  print 'teenager'
else:
  print 'kid'

names = ['Michael', 'Bob', 'Tracy']
for name in names:
  print name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  sum = sum + x
print sum

print range(5)

sum = 0
for x in range(101):
  sum = sum + x
print sum


sum = 0
n = 99
while n > 0:
  sum = sum + n
  n = n - 2
print sum 

birth = int(raw_input('birth: '))
if birth < 2000:
  print u'00前'
else:
  print u'00后'


# dict
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

d['Adam'] = 67
print d['Adam']

d['Jack'] = 90
print d['Jack']
d['Jack'] = 88
print d['Jack']

# print d['Thomas']
print 'Thomas' in d
print d.get('Thomas')
print d.get('Thomas', -1)

d.pop('Bob')
print d

key = [1, 2, 3]
# d[key] = 'a list'

# set
s = set([1, 2, 3])
print s

s = set([1, 1, 2, 2, 3, 3])
print s

s.add(4)
print s
s. add(4)
print s

s.remove(4)
print s


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

a = ['c', 'b', 'a']
a.sort()
print a

a = 'abc'
b = a.replace('a', 'A')
print b, a

