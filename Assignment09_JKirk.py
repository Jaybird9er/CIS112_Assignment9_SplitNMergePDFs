""" 
Description: 
 - Concatenates three PDF files together as "MergedFile.pdf".
Author: Jamey Kirk
Date: 05.28.2021
Assignment: 08
Class: CIS 112
"""

import pathlib
from PyPDF2 import PdfFileMerger
from pathlib import Path


""" Assignment 08
global variables
pdfMerge = PdfFileMerger()
# get directory path and sort PDFs
pdf_path = pathlib.Path.cwd()
pdf_list = list(pdf_path.glob("*.pdf"))
pdf_list.sort()

main program
# append sorted PDFs
for path in pdf_list:
    pdfMerge.append(str(path))

# write to a new PDF file
with Path("Merge.pdf").open(mode="wb") as outputFile:
    pdfMerge.write(outputFile)
"""