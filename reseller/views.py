# reseller/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reseller, ResellerUser
from .forms import ResellerUserForm
from django.contrib import messages

@login_required
def dashboard(request):
    try:
        reseller = Reseller.objects.get(user=request.user)
    except Reseller.DoesNotExist:
        return render(request, "not_reseller.html")

    users = ResellerUser.objects.filter(reseller=reseller)
    return render(request, "dashboard.html", {"users": users, "reseller": reseller})

@login_required
def create_user(request):
    reseller = Reseller.objects.get(user=request.user)
    if request.method == "POST":
        form = ResellerUserForm(request.POST)
        if form.is_valid():
            ru = form.save(commit=False)
            ru.reseller = reseller
            ru.save()
            messages.success(request, "کاربر با موفقیت اضافه شد.")
            return redirect("reseller-dashboard")
    else:
        form = ResellerUserForm()
    return render(request, "create_user.html", {"form": form})
