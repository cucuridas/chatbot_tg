import abc


class Connect(metaclass=abc.ABCMeta):
    """
    connection 클래스 생성 시 사용할 추상화 클래스입니다
    """

    @abc.abstractmethod
    def getConenction(self):
        """
        실제적인 연결에 대한 로직이 정의되는 함수입니다
        """
        pass

    @abc.abstractmethod
    def checkConnection(self):
        """
        연결 후 정상적으로 Connection이 이루어졌는가를 확인하는 함수입니다
        """
        pass
