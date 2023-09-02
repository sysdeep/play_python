from app.modules.network.network import Network
from app.modules.network.network_factory import NetworkFactory


def test_instance():

    module = NetworkFactory.create()

    assert isinstance(module, Network)


def test_synthetic():

    module = NetworkFactory.create()

    ifaces = module.get_ifaces()

    assert len(ifaces) == 1
    assert ifaces[0].name == 'eth0'
    assert ifaces[0].ip == '192.168.0.1'
