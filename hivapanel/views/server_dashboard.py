# hivapanel/views/server_dashboard.py
from django.shortcuts import render
from utils.server_status import get_all_server_status

def server_dashboard(request):
    servers = get_all_server_status()
    return render(request, "server_dashboard.html", {"servers": servers})
