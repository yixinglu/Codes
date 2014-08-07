#!/usr/bin/env python

import os
from subprocess import call


cur_dir = '.'
dirpath = []
newdirpath = []

def rename(name):
  sp = name.split()
  if len(sp) > 1:
    new_name = sp[0].upper()
    for dn in sp[1:]:
      new_name = new_name + dn[0].upper() + dn[1:].lower()
    return new_name
  return name

def walk_dir(path):
  for fd in os.listdir(path):
    re_path = os.path.join(path, fd)
    if os.path.isdir(re_path):
      walk_dir(re_path)
      dirpath.append(re_path)
      newdirpath.append(os.path.join(path, rename(fd)))

def git_rename():
  walk_dir(cur_dir)
  assert len(dirpath)==len(newdirpath), 'length is not equal.'
  for i, v in enumerate(dirpath):
    call('git', 'mv', dirpath[i], newdirpath[i])



git_rename()
