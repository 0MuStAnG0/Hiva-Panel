from django.shortcuts import render
from django.http import JsonResponse
from utils.coupons import apply_coupon

def check_coupon(request):
    code = request.GET.get("code")
    discount = apply_coupon(code)
    return JsonResponse({"discount": discount})
