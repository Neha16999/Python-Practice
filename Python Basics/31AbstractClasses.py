from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    #pass                   it will also be abstract
    def process(self):
        print("Its Running")


c=Laptop()
print(c.process())


