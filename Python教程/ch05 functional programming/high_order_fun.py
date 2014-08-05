#!/usr/bin/env python

def f(x):
  return x * x
print map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])

def add(x, y):
  return x + y
print reduce(add, [1, 3, 5, 7, 9])
print sum([1, 3, 5, 7, 9])

def fn(x, y):
  return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9])

def str2int(s):
  def fn(x, y):
    return x * 10 + y
  return reduce(fn, map(int, s))

print isinstance(str2int('13579'), int)


def str2int(s):
  return reduce(lambda x,y: x*10+y, map(int, s))
print isinstance(str2int('13579'), int)

print sorted([36, 5, 12, 9, 21])

def reversed_cmp(x, y):
  if x > y:
    return -1
  if x < y:
    return 1
  return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)

print sorted(['about', 'bob', 'Zoo', 'Credit'])

def cmp_ignore_case(s1, s2):
  u1 = s1.upper()
  u2 = s2.upper()
  if u1 < u2:
    return -1
  if u1 > u2:
    return 1
  return 0

print sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)

def calc_sum(*args):
  ax = 0
  for n in args:
    ax = ax + n
  return ax

def lazy_sum(*args):
  def sum():
    ax = 0
    for n in args:
      ax = ax + n
    return ax
  return sum

f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()
f2 = lazy_sum(1, 3, 5, 7, 9)
print f==f2


def my_map(f, L=None):
  if not L:
    L = []
  r = []
  for i in L:
    r.append(f(i))
  return# -*- coding: utf-8 -*- r

print my_map(int, '1234')
print my_map(int, ['1', '2', '3'])


def my_map(f, L=None):
  if not L:
    L = []
  r = []
  for i in L:
    r.append(f(i))
  return r

print my_map(int, '1234')
print my_map(int, ['1', '2', '3'])

