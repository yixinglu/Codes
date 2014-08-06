#!/usr/bin/env python

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
