from abc import ABC, abstractmethod
from Document import Document

class DocumentProcessor(ABC):
    # Creator 
    # factory method
    @abstractmethod
    def factory_document(self, type:str):
        pass
