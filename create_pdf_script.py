from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(results):
    pdf_filename = "jenkins_report.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 700, "Jenkins Check Results:")

    # Вставляем результаты проверок в PDF
    y_position = 680  # Начальная позиция для вставки результатов
    for result in results:
        y_position -= 20  # Размещаем каждый результат на новой строке
        c.drawString(100, y_position, result)

    c.save()
    return pdf_filename

# Пример использования:
check_results = [
    "Check 1: Passed",
    "Check 2: Failed",
    "Check 3: Passed"
]

pdf_file = create_pdf(check_results)
print(f"PDF created: {pdf_file}")