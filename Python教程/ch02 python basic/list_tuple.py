#!/usr/bin/env python

# list: sequential, changeable
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0], classmates[1], classmates[2]
# print classmates[3]
print classmates[-1], classmates[-2], classmates[-3]
# print classmates[-4]

classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates

print classmates.pop()
print classmates

classmates[1] = 'Sarah'
print classmates

L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)
print s[2][1]
L = []
print len(L)

# tuple: sequential, unchangeable
classmates = ('Michael', 'Bob', 'Tracy')
print classmates[0], classmates[-1]

t = (1, 2)
print t
t = ()
print t
t = (1)
print t
t = (1,)
print t
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t

