import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def export_to_excel(dataframe, filename):
    """Export dataframe to Excel file"""
    dataframe.to_excel(filename, index=False)
    print(f"✅ Exported to {filename}")


def export_to_pdf(dataframe, filename):
    """Export dataframe to PDF file"""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    # Convert dataframe to list of lists for the table
    data = [dataframe.columns.tolist()] + dataframe.values.tolist()
    
    # Create table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(table)
    doc.build(elements)
    print(f"✅ Exported to {filename}")
