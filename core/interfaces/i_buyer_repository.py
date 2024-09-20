from abc import abstractmethod, ABC


class IBuyerRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create_buyer(self, buyer):
        pass