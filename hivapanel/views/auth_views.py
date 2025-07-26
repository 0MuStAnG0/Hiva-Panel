from django.http import JsonResponse
from utils.auth import generate_otp, verify_otp

def request_otp(request):
    user_id = request.GET.get("user_id", "default")
    code = generate_otp(user_id)
    return JsonResponse({"otp": code})

def confirm_otp(request):
    user_id = request.GET.get("user_id")
    code = request.GET.get("code")
    valid = verify_otp(user_id, code)
    return JsonResponse({"verified": valid})
