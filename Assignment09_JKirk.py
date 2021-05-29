""" 
Description: 
 - Splits 1 PDF file, inserts a file in the middle, and merges everything into one file.

Author: Jamey Kirk
Date: 05.29.2021
Assignment: 08
Class: CIS 112
"""

import pathlib, os
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from pathlib import Path

""" global variables """

mainPDf = "pythonlearn_ch8MissingPages.pdf"
insertPDF = "From_pythonlearn_ch8.pdf"
section1 = PdfFileWriter()
section2 = PdfFileWriter()
pdfMerge = PdfFileMerger()

""" functions """

# path contstructor
def pathBuilder(fileName):
    return os.path.join(pathlib.Path.cwd(), fileName)

""" 
`for in` loop gets pages from input file and adds them to output file
"""
def getPages(n1, n2, section):
    for pageN in range (n1, n2):
        page = input_pdf.getPage(pageN)
        section.addPage(page)

""" 
after pages have been added to file, a new file is created with the user's file name
"""
def outputPDF(section):
    with Path (userFileName).open(mode="wb") as outputFile:
        section.write(outputFile)

""" main program """

# create section 1 (beginning section)
userFileName = "section1.pdf"
main_pdf_path = pathBuilder(mainPDf)
input_pdf = PdfFileReader(main_pdf_path)

getPages(0, 4, section1)
outputPDF(section1)

# create section 2 (end section)
userFileName = "section2.pdf"

getPages(4, 12, section2)
outputPDF(section2)

# list of PDFs
pdf_list = list((pathBuilder("section1.pdf"), pathBuilder("From_pythonlearn_ch8.pdf"), pathBuilder("section2.pdf")))

# append PDF list
for path in pdf_list:
    pdfMerge.append(str(path))

# write to a new PDF file
with Path("Merge.pdf").open(mode="wb") as outputFile:
    pdfMerge.write(outputFile)