import ssl
import socket


def run(target):
    if target.port != 443:
        return {"info": "Non-HTTPS port, skipping certificate"}

    ctx = ssl.create_default_context()
    try:
        with socket.create_connection((target.domain, target.port), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=target.domain) as ssock:
                cert = ssock.getpeercert()
    except Exception as e:
        return {"error": str(e)}

    return {
        "certificate": cert,
        "references": [
            f"https://crt.sh/?q={target.domain}",
        ],
    }
