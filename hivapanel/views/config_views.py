from django.http import JsonResponse
from utils.config_generator import generate_config

def get_config(request):
    uuid = request.GET.get("uuid", "test-uuid")
    server = request.GET.get("server", "vpn.example.com")
    config = generate_config(server, uuid)
    return JsonResponse({"config": config})
