#!/usr/bin/env python

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

