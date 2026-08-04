# Install PyPDF2 if not already installed:
# pip install PyPDF2
import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as '{output_filename}'")

cwd = os.getcwd()

output_folder = os.path.join(cwd, "Merged Files")
os.makedirs(output_folder, exist_ok=True)

# List all items in CWD
items = os.listdir(cwd)
print("\nItems in CWD:")

pdfs = []
count = 0
for item in items:
    if item.endswith(".pdf"):
        pdfs.append(item)
        print(count, item)
        count+=1

queue = input("Which ones do you want and in what order. Add spaces in between: ")
numbers = queue.split(" ")

strings = []

for item in numbers:
    strings.append(pdfs[int(item)])
    
y = input("Name of final file: ") + ".pdf"

output_path = os.path.join(output_folder, y)

merge_pdfs(strings, output_path)