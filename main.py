from PyPDF2 import PdfWriter, PdfReader
import os

# put all files in pdf_files folder
# make sure to run this file in the same directory where the pdf_files folder is located

pdf_files = os.listdir('pdf_files')
merger = PdfWriter()

specific_files = []

n = int(input("Enter the number of files you want to merge or enter 0 to merge all files: "))

if n != 0:
    print("Enter the names of the files you want to merge")
    for i in range(n):
        file = input(f"Enter the name of the file {i + 1}: ")
        specific_files.append(file)

print("Merging PDFs...")

if n == 0:
    for pdf in pdf_files:
        pdf_reader = PdfReader(f'pdf_files/{pdf}')
        merger.append(pdf_reader)

else:
    for i in specific_files:
        pdf_reader = PdfReader(f'pdf_files/{i}')
        merger.append(pdf_reader)

try:
    merger.write("merged-pdf.pdf")
    print("PDFs merged successfully")

except FileNotFoundError:
    print("Error")

finally:
    merger.close()
