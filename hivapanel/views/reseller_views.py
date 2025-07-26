from django.shortcuts import render
from django.http import JsonResponse

RESELLERS = []

def add_reseller(request):
    if request.method == "POST":
        username = request.POST.get("username")
        RESELLERS.append({"username": username, "clients": []})
        return JsonResponse({"status": "created"})
    return JsonResponse({"status": "error"})

def reseller_list(request):
    return render(request, "resellers.html", {"resellers": RESELLERS})
