
from abc import ABC, abstractmethod


class ClassAbstractHardware(ABC):

    def __init__(self):
        self.is_connected = False

    def connect(self, device):
        if self.is_connected is True:
            print('Cannot connect. Already connected!')
            return False

        return self._connect(device)

    @abstractmethod
    def _connect(self, device):
        return

    def disconnect(self):
        if self.is_connected is False:
            print('Cannot disconnect. Already disconnected!')
            return False

        return self._disconnect()

    @abstractmethod
    def _disconnect(self):
        return

    def getData(self):
        if self.is_connected is False:
            print('Cannot getData. Hardware disconnected!')
            return False

        return self._getData()

    @abstractmethod
    def _getData(self):
        return

    def setData(self):
        if self.is_connected is False:
            print('Cannot setData. Hardware disconnected!')
            return False

        return self._setData()

    @abstractmethod
    def _setData(self):
        return