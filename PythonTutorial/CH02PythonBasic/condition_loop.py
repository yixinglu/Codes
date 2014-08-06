#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


# loop
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

