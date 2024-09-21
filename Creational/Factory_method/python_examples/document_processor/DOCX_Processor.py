from __future__ import annotations
from Document import Document 
from DOCX_Document import DOCX_Document
from DocumentProcessor import DocumentProcessor 

class DOCX_Processor(DocumentProcessor):
    # concrete 
    def factory_document(self, type:str)->Document:
        return DOCX_Document(type)
    