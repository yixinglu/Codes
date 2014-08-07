#!/usr/bin/env python


import os

print os.name
# print os.uname()


print os.environ
print os.getenv('PATH')

print os.path.abspath('.')
print os.path.join('/Users/michael', 'testdir')

os.mkdir('testdir')
os.rmdir('testdir')

print os.path.split('/Users/michael/testdir/file.txt')
print os.path.splitext('/Users/michael/testdir/file.txt')


import shutil
shutil.copyfile('import_os.py', 'text.txt')


os.rename('text.txt', 'test.py')
os.remove('test.py')


print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

