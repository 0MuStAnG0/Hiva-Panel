# payments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment
from .forms import PaymentForm
from django.contrib import messages

@login_required
def payment_create(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            messages.success(request, "درخواست پرداخت ثبت شد. پس از بررسی تایید می‌گردد.")
            return redirect("payment-list")
    else:
        form = PaymentForm()
    return render(request, "payment_create.html", {"form": form})

@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "payment_list.html", {"payments": payments})
