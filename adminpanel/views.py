# adminpanel/views.py

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Sum
from configs.models import VPNAccount
from subscriptions.models import Plan
from django.contrib.auth.models import User

@staff_member_required
def admin_dashboard(request):
    total_users = User.objects.count()
    total_accounts = VPNAccount.objects.count()
    total_traffic = VPNAccount.objects.aggregate(total=Sum('traffic_used_gb'))['total'] or 0

    plans = Plan.objects.all()

    return render(request, "admin_dashboard.html", {
        "total_users": total_users,
        "total_accounts": total_accounts,
        "total_traffic": total_traffic,
        "plans": plans,
    })
