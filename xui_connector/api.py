# xui_connector/api.py

import requests

def create_xui_account(server, username, traffic_gb, expire_days):
    url = f"http://{server.ip_address}:{server.port}/panel/api/inbound/add"

    payload = {
        "up": 0,
        "down": 0,
        "total": int(traffic_gb * 1024 * 1024 * 1024),
        "remark": f"{username}",
        "enable": True,
        "expiryTime": expire_days * 86400,
        "listen": "",
        "port": 0,
        "protocol": "vless",
        "settings": {
            "clients": [
                {
                    "id": "auto",
                    "flow": "",
                    "email": f"{username}@hiva"
                }
            ],
            "decryption": "none",
            "fallbacks": []
        },
        "streamSettings": {
            "network": "tcp",
            "security": "none"
        },
        "sniffing": {
            "enabled": True,
            "destOverride": ["http", "tls"]
        }
    }

    headers = {
        "Authorization": f"Bearer {server.api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        inbound = data.get("obj", {})
        return {
            "id": inbound.get("id"),
            "protocol": "vless",
            "transport": "tcp",
            "uuid": inbound["settings"]["clients"][0]["id"],
        }
    else:
        raise Exception(f"X-UI پاسخ نداد: {response.text}")
