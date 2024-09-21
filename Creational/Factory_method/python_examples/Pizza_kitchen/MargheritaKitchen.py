from __future__ import annotations
from Pizza import Pizza
from PizzaKitchen import PizzaKitchen
from MargheritaPizza import MargheritaPizza

class MargheritaKitchen(PizzaKitchen):

    def create_pizza(slef, type:str, size:str, price:float)->Pizza:
        return MargheritaPizza(type, size, price)

