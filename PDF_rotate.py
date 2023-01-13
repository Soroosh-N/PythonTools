# Install PyPDF2 if not installed:
# !pip install PyPDF2

from os import walk
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# This program will take the original.pdf from root directory,
# and will rotate the pdf pages by "rotation_degree" degree
# the result will be saved in "rotated_[RD]_degree.pdf" file.

# Create rotation
RD = 90
pdf_in = open("original.pdf", 'rb')
pdf_reader = PdfFileReader(pdf_in)
pdf_writer = PdfFileWriter()
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(RD)
    pdf_writer.addPage(page)
pdf_out = open("rotated_" + str(RD) + "_degree.pdf", 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
