#!/usr/bin/env python

'id check'

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'

myInput = raw_input('Identifier to test?')
if len(myInput) > 1:
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be
		alphabetic'''
	else:
		alphnums = alphas + nums # replace alphas + nums
		for otherChar in myInput[1:]:
			if otherChar not in alphnums: # alphas + nums:
				print ''' invalid: remaining
				symbols must be alphanumeric'''
				break
			else:
				print "okey as an identifier"
