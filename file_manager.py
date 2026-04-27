import os
import PyPDF2

class PDFManager:
    def __init__(self, directory):
        self.directory = directory

    # Load all PDF files from directory
    def load_pdfs(self):
        pdf_files = []
        for file in os.listdir(self.directory):
            if file.endswith(".pdf"):
                pdf_files.append(file)
        return pdf_files

    # Get metadata of a single PDF
    def get_metadata(self, file_name):
        file_path = os.path.join(self.directory, file_name)

        file_size = os.path.getsize(file_path)  # bytes

        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

        return {
            "file_name": file_name,
            "file_size_kb": round(file_size / 1024, 2),
            "num_pages": num_pages
        }

    # List all PDFs with metadata
    def list_all_pdfs(self):
        pdf_files = self.load_pdfs()
        all_data = []

        for pdf in pdf_files:
            metadata = self.get_metadata(pdf)
            all_data.append(metadata)

        return all_data