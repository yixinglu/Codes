

class Dict(dict):
  '''
  Simple dict but also support access as x.y style.

  >>> d1 = Dict()
  >>> d1['x'] = 100
  >>> d1.x
  100
  >>> d1.y = 200
  >>> d1['y']
  200
  >>> d2 = Dict(a=1, b=2, c='3')
  >>> d2.c
  '3'
  >>> d2['empty']
  Traceback (most recent call last):
    File "D:\Program Files\Python27\lib\doctest.py", line 1315, in __run
      compileflags, 1) in test.globs
    File "<doctest __main__.Dict[7]>", line 1, in <module>
      d2['empty']
  KeyError: 'empty'
  >>> d2.empty
  Traceback (most recent call last):
    File "D:\Program Files\Python27\lib\doctest.py", line 1315, in __run
      compileflags, 1) in test.globs
    File "<doctest __main__.Dict[8]>", line 1, in <module>
      d2.empty
    File "mydict.py", line 37, in __getattr__
      raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
  AttributeError: 'Dict' object has no attribute 'empty'
  '''
  def __init__(self, **kw):
    super(Dict, self).__init__(**kw)

  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

  def __setattr__(self, key, value):
    self[key] = value


if __name__ == '__main__':
  import doctest
  doctest.testmod()
