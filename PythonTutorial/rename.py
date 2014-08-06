#!/usr/bin/env python

import os
from subprocess import call

current_dir = '.'

def change_name(root, dirname):
  splitnames = dirname.split()
  if len(splitnames) == 1:
    return
  retdir = os.path.join(root, splitnames[0].upper())
  for name in splitnames[1:]:
    retdir = retdir + name[0].upper() + name[1:].lower()
  return retdir

for root, dirs, files in os.walk(current_dir):
  for directory in dirs:
    dirname = change_name(root, directory)
    if dirname:
      call(['git', 'mv', os.path.join(root,directory), dirname])

