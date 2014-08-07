#!/usr/bin/env python


f = open('text.txt', 'w')
f.write('Hello, world!')
f.close()


with open('text.txt', 'w') as f:
  f.write('Hello, world!')
