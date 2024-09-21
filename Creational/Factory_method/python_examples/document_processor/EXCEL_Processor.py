from __future__ import annotations
from Document import Document 
from DocumentProcessor import DocumentProcessor 
from EXCEL_Document import EXCEL_Document 

class EXCEL_Processor(DocumentProcessor):
    # concrete 
    def factory_document(self, type:str)->Document:
        return EXCEL_Document(type)
    