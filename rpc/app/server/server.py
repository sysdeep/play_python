from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from app.modules.network.network_factory import NetworkFactory
# from app.modules.network.network import Network


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class Server:
    # __network = None

    def __init__(self):
        pass

    def start(self, addr: str, port: int):

        network = NetworkFactory.create()

        # Create server
        with SimpleXMLRPCServer((addr, port), allow_none=True,
                                requestHandler=RequestHandler) as server:
            server.register_introspection_functions()

           # Register pow() function; this will use the value of
           # pow.__name__ as the name, which is just 'pow'.
           # server.register_function(pow)

           # Register a function under a different name
            def adder_function(x, y):
                return x + y

            server.register_function(adder_function, 'add')

            server.register_function(
                lambda: network.get_ifaces(), 'network_get_ifaces')
            server.register_function(
                network.set_hostname, 'network_set_hostname')
            server.register_function(
                network.get_hostname, 'network_get_hostname')
            # Register an instance; all the methods of the instance are
            # published as XML-RPC methods (in this case, just 'mul').

            # class MyFuncs:
            #     def mul(self, x, y):
            #         return x * y
            # #
            # server.register_instance(MyFuncs(), allow_dotted_names=True)
            # #
            # server.register_instance(network, allow_dotted_names=True)

            # Run the server's main loop
            server.serve_forever()

        # NOTE: не очень заработало.. - точнее не заработало
        # @property
        # def _network(self) -> Network:
        #
        #     if self.__network is None:
        #         self.__network = NetworkFactory.create()
        #
        #     return self.__network
