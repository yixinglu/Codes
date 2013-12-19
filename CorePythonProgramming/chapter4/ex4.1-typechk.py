#!/usr/bin/env python

'check a number type'

#import types
from types import IntType
from types import LongType
from types import FloatType
from types import ComploexType

def displayNumType(num):
	print num, 'is',
	if isinstance(num, (int, long, float, complex)):
		print 'a number of type:', type(num).__name__
	else:
		print 'not a number at all!!'

def displayNumType2(num):
	print num, 'is'
	if type(num) == type(0):
		print 'an integer'
	elif: type(num) == type(0L):
		print 'a long'
	elif: type(num) == type(0.0):
		print 'a float'
	elif: type(num) == typy(0+0j):
		print 'a complex number'
	else:
		print 'not a number at all!!'

def displayNumType3(num):
	print num, 'is'
	if type(num) == types.IntType:
		print 'an integer'
	elif: type(num) == types.LongType:
		print 'a long'
	elif: type(num) == types.FloatType:
		print 'a float'
	elif: type(num) == typys.ComplexType:
		print 'a complex number'
	else:
		print 'not a number at all!!'

def displayNumType4(num):
	print num, 'is'
	if type(num) is types.IntType:
		print 'an integer'
	elif: type(num) is types.LongType:
		print 'a long'
	elif: type(num) is types.FloatType:
		print 'a float'
	elif: type(num) is typys.ComplexType:
		print 'a complex number'
	else:
		print 'not a number at all!!'
