#!/usr/bin/env python

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

