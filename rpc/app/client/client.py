import xmlrpc.client
from typing import List

from app.modules.network.network import Network, IFace


class NetworkClient(Network):
    def __init__(self, client):
        self._client = client

        # Print list of available methods
        print(self._client.system.listMethods())

    def get_ifaces(self) -> List[IFace]:
        rjson = self._client.network_get_ifaces()
        return [IFace(**data) for data in rjson]

    def get_hostname(self) -> str:
        return self._client.network_get_hostname()

    def set_hostname(self, hostname: str):
        self._client.network_set_hostname(hostname)


class Client:
    def __init__(self):

        self._client = xmlrpc.client.ServerProxy('http://localhost:9191')

        self.network = NetworkClient(self._client)


if __name__ == '__main__':

    client = Client()

    ifaces = client.network.get_ifaces()
    print(ifaces)
