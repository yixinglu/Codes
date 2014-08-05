#!/usr/bin/env python

def my_map(f, L=None):
  if not L:
    L = []
  r = []
  for i in L:
    r.append(f(i))
  return r

print my_map(int, '1234')
print my_map(int, ['1', '2', '3'])

print map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def build(x, y):
  return lambda: x * x + y * y

print build(2, 3)()
