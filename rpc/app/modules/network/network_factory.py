
from app.modules.network.network import Network
from app.modules.network.network_impl import NetworkImpl


class NetworkFactory:

    @classmethod
    def create(cls) -> Network:
        return NetworkImpl()
