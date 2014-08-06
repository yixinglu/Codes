#!/usr/bin/env python

import hello

hello.test()
print hello.__doc__
print hello.__author__


try:
  import cStringIO as StringIO
except ImportError:
  import StringIO


try:
  import json # python >= 2.6
except ImportError:
  import simplejson as json # python <= 2.5

