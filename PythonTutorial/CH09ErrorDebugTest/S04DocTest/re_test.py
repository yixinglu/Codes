#!/usr/bin/env python

import re


m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)

