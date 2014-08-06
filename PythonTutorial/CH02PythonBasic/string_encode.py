#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Unicode
'''
1. ASCII编码是1个字节，而Unicode编码通常是2个字节
2. ASCII编码实际上可以被看成是UTF-8编码的一部分
3. 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
'''

print ord('A')
print chr(65)

print u'中文'
print u'中'
print u'中文'.encode('utf-8')

print u'\u4e2d'
print u'ABC'.encode('utf-8')

print len(u'ABC')
print len('ABC')

print len(u'中文')

print len('\xe4\xb8\xad\xe6\x96\x87')

print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# format string output
print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%d.' % ('Michael', 100000)

print '%2d-%02d' % (3, 1)
print '%.2f' % 3.1415926
print 'Age: %s. Gender: %s' % (25, True)

print u'Hi, %s' % u'Michael'
print 'growth rate: %d %%' % 7
print u'中文'.encode('gb2312')
