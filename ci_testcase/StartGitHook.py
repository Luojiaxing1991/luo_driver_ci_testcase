#! /usr/bin/env python

from wsgiref.simple_server import make_server

def application(environ,start_response):
    os.system('Get the web hook')
    return [b'Hello webhook']


httpd = make_server('',9123,application)

httpd.serve_forever()


