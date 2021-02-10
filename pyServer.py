#!/usr/bin/python3
import http.server
import socketserver

hostName = "0.0.0.0"
hostPort = 4000

class MyServer(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyServer

myServer = socketserver.TCPServer(("", hostPort), handler_object)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
