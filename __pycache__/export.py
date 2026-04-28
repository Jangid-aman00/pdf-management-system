from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import letter

# Export to Excel
def export_to_excel(df, filename):
    df.to_excel(filename, index=False)

# Export to PDF
def export_to_pdf(df, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data)

    doc.build([table])
    