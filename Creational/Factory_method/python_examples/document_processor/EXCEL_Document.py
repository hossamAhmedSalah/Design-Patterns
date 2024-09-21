from abc import ABC
from Document import Document 

class EXCEL_Document(Document):
    def __init__(self, type="excel"):
        super().__init__(type)

    def open(self):
        print(f"Open the {self.type} file")
    def save(self):
        print(f"Save the {self.type} file")
    def close(self):
        print(f"Close the {self.type} file")
    