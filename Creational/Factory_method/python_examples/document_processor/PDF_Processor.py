from __future__ import annotations
from Document import Document 
from DocumentProcessor import DocumentProcessor 
from PDF_Document import PDF_Document

class PDF_Processor(DocumentProcessor):
    # concrete 
    def factory_document(self, type:str)->Document:
        return PDF_Document(type)
    