from abc import ABC, abstractmethod 
from Document import Document

class PDF_Document(Document):
    def __init__(self, type="pdf"):
        super().__init__(type)
        

    def open(self):
        print(f"Open the {self.type} file")
    def save(self):
        print(f"Save the {self.type} file")
    def close(self):
        print(f"Close the {self.type} file")