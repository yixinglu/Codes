#!/usr/bin/env python


try:
  f = open('test.txt', 'r')
  print f.read()
finally:
  if f:
    f.close()


with open('test.txt', 'r') as f:
  print f.read()


with open('test.txt', 'r') as f:
  for line in f.readlines():
    print(line.strip())



with open('test.jpg', 'rb') as f:
  f.read()


with open('gbk.txt', 'rb') as f:
  print f.read().decode('gbk')


import codecs

with codecs.open('gbk.txt', 'r', 'gbk') as f:
  print f.read()
