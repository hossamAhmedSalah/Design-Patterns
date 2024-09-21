from abc import ABC, abstractmethod
from Document import Document 

class DOCX_Document(Document):
    def __init__(self, type="docx"):
        super().__init__(type)
        
    def open(self):
        print(f"Open the {self.type} file")
    def save(self):
        print(f"Save the {self.type} file")
    def close(self):
        print(f"Close the {self.type} file")