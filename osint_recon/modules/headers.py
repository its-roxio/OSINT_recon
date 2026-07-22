import requests


def run(target):
    url = f"{target.scheme}://{target.domain}:{target.port}{target.path}"
    try:
        resp = requests.get(url, timeout=10)
        headers = dict(resp.headers)
    except Exception as e:
        return {"error": str(e)}

    security = {
        k: v
        for k, v in headers.items()
        if k.lower().startswith("x-") or "security" in k.lower()
    }

    return {
        "url": url,
        "status_code": resp.status_code,
        "headers": headers,
        "security_headers": security,
        "references": [
            f"https://observatory.mozilla.org/analyze/{target.domain}",
        ],
    }
