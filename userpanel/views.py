# userpanel/views.py

import io
import qrcode
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.subscription import build_subscription_links
from configs.models import VPNAccount

@login_required
def dashboard(request):
    user = request.user
    accounts = VPNAccount.objects.filter(user=user)

    results = []
    for acc in accounts:
        link = build_subscription_links(acc)
        qr = qrcode.make(link)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        qr_img = buffer.getvalue()

        results.append({
            'server': acc.server.name,
            'link': link,
            'qr': qr_img.hex(),
            'expire': acc.expire_date,
            'traffic': f"{acc.traffic_used_gb}/{acc.traffic_limit_gb} GB",
        })

    return render(request, "dashboard.html", {"accounts": results})
