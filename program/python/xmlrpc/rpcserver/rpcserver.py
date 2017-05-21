from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

from wxcs import * 
import socket
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
def adder_function(x,y):
    return x + y

class MyFuncs:
    def div(self, x, y):
        return x // y

class XMLRPCServer ():
    def __init__(self):
        self.port=8000;
        self.host=socket.gethostname();
        self.server=SimpleXMLRPCServer((self.host, self.port),
                                       requestHandler=RequestHandler);
        self.server.register_introspection_functions();

    def server_init(self):
        self.server.register_function(pow)
        self.server.register_function(adder_function, 'add')
        self.server.register_instance(wxcs());
        # self.server.register_instance(MyFuncs());
        
    def serve_forever(self):
        self.server.serve_forever();
