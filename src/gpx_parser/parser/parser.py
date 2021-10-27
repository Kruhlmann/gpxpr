import abc


class Parser(abc.ABC):
    @abc.abstractmethod
    def parse(self):
        raise NotImplementedError()
