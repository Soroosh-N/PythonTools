# If not installed, install this lib first:
# pip install pdf2image

from pdf2image import convert_from_path

INPUT_PDF_NAME = "input_pdf.pdf"
DPI = 100
TARGET_FORMAT = "JPEG"

pages = convert_from_path(INPUT_PDF_NAME, DPI)
for idx, page in enumerate(pages):
    page.save("page_" + str(idx) + ".jpg", TARGET_FORMAT)
