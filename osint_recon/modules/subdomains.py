import requests


def _get_json(url):
    try:
        resp = requests.get(url, timeout=10)
        if resp.headers.get("content-type", "").startswith("application/json"):
            return resp.json()
    except Exception:
        return None
    return None


def _from_crtsh(domain: str):
    url = f"https://crt.sh/?q={domain}&output=json"
    data = _get_json(url)
    if not data:
        return set()
    found = set()
    for entry in data:
        name_value = entry.get("name_value")
        if not name_value:
            continue
        for part in name_value.split("\n"):
            part = part.strip()
            if part.endswith(domain):
                found.add(part)
    return found


def _from_buffover(domain: str):
    url = f"https://dns.bufferover.run/dns?q=.{domain}"
    data = _get_json(url)
    if not data:
        return set()
    found = set()
    for key in ("FDNS_A", "RDNS"):
        for entry in data.get(key, []):
            parts = entry.split(",")
            if len(parts) == 2 and parts[1].endswith(domain):
                found.add(parts[1].strip())
    return found


def _from_threatcrowd(domain: str):
    url = f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
    data = _get_json(url)
    if not data:
        return set()
    subs = data.get("subdomains", []) or []
    return {s.strip() for s in subs if s.endswith(domain)}


def _from_threatminer(domain: str):
    url = f"https://api.threatminer.org/v2/domain.php?q={domain}&rt=5"
    data = _get_json(url)
    if not data:
        return set()
    subs = data.get("results", []) or []
    return {s.strip() for s in subs if isinstance(s, str) and s.endswith(domain)}


def run(target):
    domain = target.domain
    all_subs = set()

    sources = {
        "crt.sh": _from_crtsh,
        "BuffOver": _from_buffover,
        "ThreatCrowd": _from_threatcrowd,
        "ThreatMiner": _from_threatminer,
    }

    source_results = {}

    for name, func in sources.items():
        subs = func(domain)
        source_results[name] = sorted(subs)
        all_subs.update(subs)

    return {
        "subdomains": sorted(all_subs),
        "by_source": source_results,
        "references": [
            f"https://crt.sh/?q={domain}",
            f"https://dns.bufferover.run/dns?q=.{domain}",
            f"https://www.threatcrowd.org/domain.php?domain={domain}",
            f"https://www.threatminer.org/domain.php?q={domain}&rt=5",
        ],
    }
