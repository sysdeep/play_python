from typing import List

from app.modules.network.network import Network, IFace


class NetworkImpl(Network):
    def __init__(self):
        self._hostname = 'example-hostname'

    def get_ifaces(self) -> List[IFace]:
        return [IFace('eth0', '192.168.0.1')]

    def get_hostname(self) -> str:
        return self._hostname

    def set_hostname(self, hostname: str):
        print('network - set_hostname: ' + hostname)
        self._hostname = hostname
