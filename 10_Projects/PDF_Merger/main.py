from PyPDF2 import PdfWriter

merger = PdfWriter()

def merge_pdfs(pdf_list, output_path):
    '''
    pdf_list: List of PDF file paths to merge
    output_path: Path to save the merged PDF
    '''
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

nof = int(input("Enter the number of PDF files to merge: "))
pdf_files = []
for i in range(nof):
    pdf_path = input(f"Enter the path for PDF file {i + 1}: ")
    pdf_files.append(pdf_path)
output_file = input("Enter the output file name (with .pdf extension): ")

merge_pdfs(pdf_files, output_file)