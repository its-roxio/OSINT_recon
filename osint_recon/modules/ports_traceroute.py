import socket

COMMON_PORTS = [80, 443, 21, 22, 25, 53, 110, 143, 8080]


def run_ports(target):
    results = {}
    for port in COMMON_PORTS:
        try:
            with socket.create_connection((target.domain, port), timeout=1):
                results[port] = "open"
        except Exception:
            results[port] = "closed"
    return {"ports": results}


def run_trace(target):
    return {"info": "Traceroute not implemented (placeholder)"}
