from django.http import JsonResponse
from utils.email_sender import send_notification_email

def notify_user(request):
    to = request.GET.get("to", "user@example.com")
    subject = request.GET.get("subject", "اعلان Hiva Panel")
    content = request.GET.get("content", "حساب شما با موفقیت فعال شد.")
    result = send_notification_email(to, subject, content)
    return JsonResponse({"sent": result})
