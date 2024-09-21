from DOCX_Processor import DOCX_Processor 
from EXCEL_Processor import EXCEL_Processor
from PDF_Processor import PDF_Processor

docx_processor = DOCX_Processor()
document1 = docx_processor.factory_document("docx")
document1.open()
document1.save()
document1.close()

excel_processor = EXCEL_Processor()
document2 = excel_processor.factory_document("excel")
document2.open()
document2.save()
document2.close()

pdf_processor = PDF_Processor()
document3 = pdf_processor.factory_document("pdf")
document3.open();document3.save();document3.close()
