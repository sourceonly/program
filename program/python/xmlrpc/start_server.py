

from rpcserver.rpcserver import *


server=XMLRPCServer();
server.server_init();
server.serve_forever();

