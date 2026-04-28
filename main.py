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
from data_processor import DataProcessor
from export import export_to_excel, export_to_pdf

print("\n DATA PROCESSING MODULE\n")

# Load tables
processor = DataProcessor("data/table1.csv", "data/table2.csv")

# Merge tables
merged = processor.merge_tables("id")

# Select columns
selected = processor.select_columns(merged, ["id", "name", "salary"])

# Filter data
filtered = processor.filter_data(selected, "salary", 50000)

# Preview
print("Preview:\n", processor.preview(filtered))

# Export
export_to_excel(filtered, "output.xlsx")
export_to_pdf(filtered, "output.pdf")

print("✅ Excel & PDF generated")
    