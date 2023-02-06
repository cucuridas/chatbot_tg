import abc


class Connect(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getConenction(self):
        pass

    @abc.abstractmethod
    def checkConnection(self):
        pass
