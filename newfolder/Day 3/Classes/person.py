from abc import *
class Person (metaclass= ABCMeta):

    uniqueID: int = 0
    @abstractmethod
    def __init__(self,name):
        self._name = name
        Person.uniqueID += 1

    def __str__(self):
        return f"{self._name}: ID: {self.uniqueID}"


