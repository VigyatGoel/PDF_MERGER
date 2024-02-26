from PyPDF2 import PdfWriter, PdfReader
import os


def merge_pdfs(pdf_files, output_file):
    merger = PdfWriter()
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        merger.append(pdf_reader)
    try:
        merger.write(output_file)
        print("PDFs merged successfully")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        merger.close()


def main():
    pdf_files = os.listdir('pdf_files')
    # Filter out non-PDF files
    pdf_files = [file for file in pdf_files if file.endswith('.pdf')]
    n = int(input("Enter the number of files you want to merge or enter 0 to merge all files: "))
    if n != 0:
        print("Enter the names of the files you want to merge")
        specific_files = [input(f"Enter the name of the file {i + 1}: ") for i in range(n)]
        pdf_files = [f'pdf_files/{file}' for file in specific_files]
    else:
        confirm = input("Are you sure you want to merge all files? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Exiting...")
            return
    output_file = input("Enter the name of the output file: ")
    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()
