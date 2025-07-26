from django.http import FileResponse
from utils.pdf_generator import generate_pdf_report

def download_pdf_report(request):
    username = request.GET.get("username", "کاربر تست")
    usage = request.GET.get("usage", 4.5)
    traffic = request.GET.get("traffic", 15.0)
    path = "/tmp/report.pdf"
    generate_pdf_report(username, usage, traffic, path)
    return FileResponse(open(path, "rb"), as_attachment=True, filename="report.pdf")
