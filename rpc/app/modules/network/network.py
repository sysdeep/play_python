from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class IFace:
    name: str
    ip: str


class Network(ABC):

    @abstractmethod
    def get_ifaces(self) -> List[IFace]:
        pass

    @abstractmethod
    def get_hostname(self) -> str:
        pass

    @abstractmethod
    def set_hostname(self, hostname: str):
        pass
