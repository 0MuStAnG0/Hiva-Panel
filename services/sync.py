# services/sync.py

from datetime import timedelta
from django.utils import timezone
from zones.models import Server
from configs.models import VPNAccount
from subscriptions.models import Plan
from xui_connector.api import create_xui_account

def create_vpn_accounts(user, plan):
    servers = Server.objects.filter(is_active=True).order_by('?')[:plan.multi_server_count]
    expire_date = timezone.now() + timedelta(days=plan.duration_days)

    results = []

    for server in servers:
        try:
            xui_response = create_xui_account(
                server=server,
                username=str(user.id),
                traffic_gb=plan.traffic_gb,
                expire_days=plan.duration_days
            )

            account = VPNAccount.objects.create(
                user=user,
                server=server,
                inbound_id=xui_response['id'],
                protocol=xui_response['protocol'],
                transport=xui_response['transport'],
                expire_date=expire_date,
                traffic_limit_gb=plan.traffic_gb
            )
            results.append(account)
        except Exception as e:
            print(f"❌ خطا در ساخت اکانت روی سرور {server.name}: {e}")

    return results
