from file_manager import PDFManager

# Folder where PDFs are stored
PDF_DIRECTORY = "pdfs"

manager = PDFManager(PDF_DIRECTORY)

# Load PDFs
pdf_files = manager.load_pdfs()
print("\n📂 PDF Files Found:")
for file in pdf_files:
    print("-", file)

# Show metadata
print("\n📊 PDF Metadata:")
all_pdfs = manager.list_all_pdfs()

for pdf in all_pdfs:
    print(f"""
File Name   : {pdf['file_name']}
File Size   : {pdf['file_size_kb']} KB
No. of Pages: {pdf['num_pages']}
---------------------------""")
    