from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

TICKETS = []

def ticket_list(request):
    return render(request, "tickets.html", {"tickets": TICKETS})

def submit_ticket(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        TICKETS.append({"subject": subject, "message": message, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})
