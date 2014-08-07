#!/usr/bin/env python

import os


def _search(s, path):
  for fd in os.listdir(path):
    if path != '.':
      fd = os.path.join(path, fd)
    if os.path.isfile(fd):
      filename = os.path.split(fd)[1]
      if filename.find(s) != -1:
        print fd
    elif os.path.isdir(fd):
      _search(s, fd)

def search(s):
  _search(s, '.')


if __name__ == '__main__':
  search('py')
    
