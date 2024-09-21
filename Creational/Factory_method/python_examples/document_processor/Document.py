from abc import ABC, abstractmethod 
class Document(ABC):
    # interface of Document
    def __init__(self, type:str):
        self.type = type 
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def close(self):
        pass