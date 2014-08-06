#!/usr/bin/env python

from hello import Hello

h = Hello()
h.hello()

print(type(Hello))
print(type(h))


def fn(self, name='world'):
  print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()

print(type(Hello))
print(type(h))
