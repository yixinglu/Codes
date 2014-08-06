#!/usr/bin/env python
# -*- coding: utf-8 -*-

print type(123)
print type('str')
print type(None)

print type(abs)

class Animal(object):
  pass

a = Animal()
print type(a)


print type(123)==type(456)
print type('abc')==type('123')
print type('abc')==type(123)


import types

print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
print type(int)==type(str)==types.TypeType


class Dog(Animal):
  pass

class Husky(Dog):
  pass

a = Animal()
d = Dog()
h = Husky()

print isinstance(h, Husky)
print isinstance(h, Dog)
print isinstance(h, Animal)
print isinstance(d, Dog) and isinstance(d, Animal)
print isinstance(d, Husky)

print isinstance('a', str)
print isinstance(u'a', unicode)
print isinstance('a', unicode)

print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))
print isinstance(u'a', basestring)


print dir('ABC') # 要获得一个对象的所有属性和方法

print len('ABC')
print 'ABC'.__len__()


class MyObject(object):
  def __init__(self):
    self.x = 9
  def power(self):
    return self.x * self.x
  def __len__(self):
    return 100


obj = MyObject()
print len(obj)

print 'ABC'.lower()

print hasattr(obj, 'x')
print obj.x

print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y

print getattr(obj, 'z', 404)
# print getattr(obj, 'z') # error


print hasattr(obj, 'power')
print getattr(obj, 'power')

fn = getattr(obj, 'power')
print fn
print fn()


# sum = obj.x + obj.y
# sum = getattr(obj, 'x') + getattr(obj, 'y')


def readImage(fp):
  if hasattr(fp, 'read'):
    return readData(fp)
  return None

