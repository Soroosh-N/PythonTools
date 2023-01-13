# If PyPDF2 is not installed, install it:
# !pip install PyPDF2
from os import walk
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# Put all your pdfs on "pdf_directory" and then run the file
# It will merge all the pdfs together (alphabetically)

pdf_directory = 'pdfs_folder'
output = "result_pdf_name"

root, dirs, file_name = next(walk(pdf_directory))
merger = PdfFileMerger()
for pdf in file_name:
    merger.append(pdf_directory + '/' + pdf)
merger.write(output + ".pdf")
merger.close()
