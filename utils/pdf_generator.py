from fpdf import FPDF

def generate_pdf_report(username, usage, traffic, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hiva Panel - گزارش مصرف", ln=True, align="C")
    pdf.cell(200, 10, txt=f"کاربر: {username}", ln=True)
    pdf.cell(200, 10, txt=f"میزان استفاده: {usage} گیگ", ln=True)
    pdf.cell(200, 10, txt=f"ترافیک باقی‌مانده: {traffic} گیگ", ln=True)
    pdf.output(output_path)
    return output_path
