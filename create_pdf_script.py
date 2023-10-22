from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(results):
    pdf_filename = "jenkins_report.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 700, "Jenkins Check Results:")

    # Вставьте результаты проверок в PDF

    c.save()
    return pdf_filename
