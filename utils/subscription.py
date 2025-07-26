# utils/subscription.py

from urllib.parse import quote

def build_vless_url(account, server, uuid):
    return f"vless://{uuid}@{server.ip_address}:{account.port}?encryption=none&security=none&type={account.transport}#{quote(account.user.username)}"

def build_subscription_links(account):
    protocol = account.protocol.lower()
    if protocol == "vless":
        return build_vless_url(account, account.server, account.inbound_id)
    else:
        return "پروتکل هنوز پشتیبانی نمی‌شود"
