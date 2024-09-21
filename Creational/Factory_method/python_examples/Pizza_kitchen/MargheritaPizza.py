from __future__ import annotations
from Pizza import Pizza

class MargheritaPizza(Pizza):
    def __init__(self, type="Margherita", size="small", price=99.99):
        super().__init__(type, size, price)
    
    def bake(self):
        print(f"backing {self.type} {self.type} with {self.price}")
    def cut(self, slices:int = 8):
        print(f"cutting {self.type} into {slices} slices")
    def pack(self):
        print(f"Packaging the {self.type} pizza")


