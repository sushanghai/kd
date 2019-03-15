from xmlrpc.server import SimpleXMLRPCServer
def ServerA():
    servver = SimpleXMLRPCServer(("localhost",9200),allow_none=True)
    servver.register_function(hello())
def hello():
    print("hello")

ServerA()