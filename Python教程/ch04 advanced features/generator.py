#!/usr/bin/env python

# generator
L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
print g.next(), g.next(), g.next(), g.next()
for n in g:
  print n

def fab(max):
  n, a, b = 0, 0, 1
  while n < max:
    print b
    a, b = b, a + b
    n = n + 1
print fab(6)


def fab(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
print fab(6)

def odd():
  print 'step 1'
  yield 1
  print 'step 2'
  yield 3
  print 'stemp 3'
  yield 5

o = odd()
print o.next()
print o.next()
print o.next()

for n in fab(6):
  print n
