import cgi,cgitb
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

class myHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Uri',self.path)
        self.send_header('Server','OS 1.0.0')
        self.end_headers()
        self.wfile.write("hi this is test")

server_address = ('0.0.0.0',port)
Handler.protocol_version = Protocol
httpd = Server(server_address,myHandler)
sa = httpd.socket.getsockname()
print "Servering HTTP on",sa[0],"port",sa[1],"..."
httpd.serve_forever()
