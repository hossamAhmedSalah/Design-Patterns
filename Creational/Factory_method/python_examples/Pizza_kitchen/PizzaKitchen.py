from __future__ import annotations 
from Pizza import Pizza
from abc import ABC, abstractmethod 

class PizzaKitchen(ABC):
    # creator 
    # factory method 
    @abstractmethod
    def create_pizza(slef, type:str, size:str, price:float)->Pizza:
        pass