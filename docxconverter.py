from pdf2docx import Converter

pdf_file = 'images/ANN_MUCHIRI_CV'
docx_file = 'sample.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close