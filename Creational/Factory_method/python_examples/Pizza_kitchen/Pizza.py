from __future__ import annotations
from abc import ABC, abstractmethod

class Pizza(ABC):
    # piza (product) interface
    def __init__(self,type:str, size:str, price:float):
        self.type = type
        self.size = size
        self.price = float
    
    @abstractmethod
    def bake(self):
        pass
    
    @abstractmethod
    def cut(self, slices:int = 8):
        pass

    @abstractmethod
    def pack(self):
        pass

