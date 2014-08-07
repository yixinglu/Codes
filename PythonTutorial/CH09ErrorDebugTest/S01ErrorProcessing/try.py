#!/usr/bin/env python


try:
  print 'try...'
  r = 10 / int('a')
  print 'result:', r
except ValueError, e:
  print 'ValueError:', e
except ZeroDivisionError, e:
  print 'except:', e
else:
  print 'no error!'
finally:
  print 'finally...'
print 'END'



try:
  foo()
except StandardError, e:
  print 'StandardError'
except ValueError, e:
  print 'ValueError'



def foo(s):
  return 10 / int(s)

def bar(s):
  return foo(s) * 2

def main():
  try:
    bar('0')
  except StandardError, e:
    print 'Error!'
  finally:
    print 'finally...'


