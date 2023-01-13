from os import walk
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# Put all your pdfs on pdf_directory and then run the app
# It will merge all the pdfs together (alpha)

pdf_directory = 'pdfs'
output = "result"

root, dirs, file_name = next(walk(pdf_directory))
merger = PdfFileMerger()
for pdf in file_name:
    merger.append(pdf_directory + '/' + pdf)
merger.write(output + ".pdf")
merger.close()

# Create rotation
rotation_degree = 90
pdf_in = open(output + ".pdf", 'rb')
pdf_reader = PdfFileReader(pdf_in)
pdf_writer = PdfFileWriter()
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(rotation_degree)
    pdf_writer.addPage(page)
pdf_out = open("rotated_" + str(rotation_degree) + "_degree.pdf", 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
