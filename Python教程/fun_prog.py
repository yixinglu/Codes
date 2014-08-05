#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
  return r

print my_map(int, '1234')
print my_map(int, ['1', '2', '3'])

print map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def build(x, y):
  return lambda: x * x + y * y

print build(2, 3)()

def now():
  print '2013-12-25'

f = now
print f()
print now.__name__
print f.__name__

# decorator
def log(func):
  def wrapper(*args, **kw):
    print 'call %s():' % func.__name__
    return func(*args, **kw)
  return wrapper

@log
def now2():
  print '2013-12-25'

now2()
now = log(now)
now()

def log2(text):
  def decorator(func):
    def wrapper(*args, **kw):
      print '%s %s():' % (text, func.__name__)
      return func(*args, **kw)
    return wrapper
  return decorator

@log2('execute')
def now3():
  print '2013-12-25'

now3()
print now3.__name__


import functools

def log3(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    print 'call %s():' % func.__name__
    return func(*args, **kw)
  return wrapper


def log4(text):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
      print '%s %s():' % (text, func.__name__)
      return func(*args, **kw)
    return wrapper
  return decorator

@log4('execute')
def now4():
  print '2013-12-25'

now4()
print now4.__name__


def newlog(text):
  if isinstance(text, str):
    def decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kw):
        print '%s %s():' % (text, func.__name__)
        func(*args, **kw)
      return wrapper
    return decorator
  else:
    func = text
    @functools.wraps(func)
    def wrapper(*args, **kw):
      print 'call %s():' % func.__name__
      func(*args, **kw)
    return wrapper


@newlog
def now5():
  print '2013-12-25'

@newlog('execute new')
def now6():
  print '2013-12-25'

print now5
now5()
print now5.__name__
now6()
print now6.__name__


# partial function
print int('12345')
print int('12345', base=8)
print int('12345',16)

def int2(x, base=2):
  return int(x, base)

print int2('1000000')
print int2('1010101')

int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')
