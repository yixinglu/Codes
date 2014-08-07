#!/usr/bin/env python


class FooError(StandardError):
  pass

def foo(s):
  n = int(s)
  if n==0:
    raise FooError('invalid value: %s' % s)
  return 10 / n


def bar(s):
  try:
    return foo(s) * 2
  except StandardError, e:
    print 'Error!'
    raise


def main():
  bar('0')


main()


try:
  10 / 0
except ZeroDivisionError:
  raise ValueError('input error!')
