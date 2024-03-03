import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfWriter, PdfReader


def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    return files


def merge_pdfs(pdf_files, output_file):
    merger = PdfWriter()
    for pdf in pdf_files:
        try:
            pdf_reader = PdfReader(pdf)
            merger.append(pdf_reader)
        except Exception as e:
            print(f"Error: {e}")
            continue
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
    pdf_files = open_file_dialog()
    if not pdf_files:
        print("No PDF files selected.")
        return

    output_file = input("Enter the name of the output file: ")
    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()
