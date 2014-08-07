#!/usr/bin/env python

from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8889, application)
print "Serving HTTP on port 8889..."
httpd.serve_forever()
