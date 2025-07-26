import json

def generate_config(server_url, uuid, protocol="vless", transmission="tcp"):
    return json.dumps({
        "v": "2",
        "ps": "HivaVPN",
        "add": server_url,
        "port": "443",
        "id": uuid,
        "aid": "0",
        "net": transmission,
        "type": "none",
        "host": "",
        "path": "",
        "tls": "tls",
        "sni": "",
        "alpn": ["http/1.1"],
        "protocol": protocol
    }, indent=2)
