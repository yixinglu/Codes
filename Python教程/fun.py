#!/usr/bin/env python
# -*- coding: utf-8 -*-


r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3

print abs(100)
print abs(-20)
print abs(12.34)

# abs(1, 2)
# abs('a')

print cmp(1, 2)
print cmp(2, 1)
print cmp(3, 3)

print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool('')

a = abs
print a(-1)


# define a function
def my_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x

# pass
def nop():
  pass

age = 1
if age >= 18:
  pass

# my_abs(1, 2)
# print my_abs('A')
# print abs('A')


import math

def move(x, y, step, angle=0):
  nx = x + step * math.cos(angle)
  ny = y + step * math.sin(angle)
  return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y


r = move(100, 100, 60, math.pi / 6)
print r

def power(x):
  return x * x

print power(5), power(15)

def power(x, n=2):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x
  return s

print power(5, 2), power(5, 3)
print power(4)

# 默认参数必须指向不变对象！
def add_end(L=[]):
  L.append('END')
  return L

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])

print add_end()
print add_end()
print add_end()

def add_end(L=None):
  if L is None:
    L = []
  L.append('END')
  return L

print add_end()
print add_end()

def calc(numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

print calc([1, 2, 3])
print calc([1, 3, 5, 7])

def calc(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

print calc(1, 2)
print calc()

nums = [1, 2, 3]
print calc(nums[0], nums[1], nums[2])
print calc(*nums)

def person(name, age, **kw):
  print 'name:', name, 'age:', age, 'other:', kw

print person('Michael', 30)
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, city=kw['city'], job=kw['job'])
print person('Jack', 24, **kw)

def func(a, b, c=0, *args, **kw):
  print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

print func(1, 2)
print func(1, 3, c=3)
print func(1, 2, 3, 'a', 'b')
print func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
print func(*args, **kw)


def fact(n):
  if n == 1:
    return 1
  return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)
# print fact(1000)


from recipe_474088_1 import tail_call_optimized

def fact(n):
  return fact_iter(1, 1, n)

@tail_call_optimized
def fact_iter(product, count, max):
  if count > max:
    return product
  return fact_iter(product * count, count + 1, max)

print fact(1000)

