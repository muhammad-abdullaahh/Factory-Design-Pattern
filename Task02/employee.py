from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def position(self):
        pass