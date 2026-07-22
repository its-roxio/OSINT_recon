import dns.resolver

try:
    import whois as python_whois
except ImportError:
    python_whois = None


def run_whois(target):
    if not python_whois:
        return {"error": "python-whois not installed"}

    try:
        data = python_whois.whois(target.domain)
        raw = data.text if hasattr(data, "text") else str(data)
    except Exception as e:
        return {"error": str(e)}

    return {
        "raw": raw,
        "references": [
            f"https://whois.domaintools.com/{target.domain}",
        ],
    }


def run_dns(target):
    records = {}
    resolver = dns.resolver.Resolver()
    for rtype in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = resolver.resolve(target.domain, rtype)
            records[rtype] = [str(r) for r in answers]
        except Exception:
            records[rtype] = []

    return {
        "records": records,
        "references": [
            f"https://dnslytics.com/domain/{target.domain}",
            f"https://securitytrails.com/domain/{target.domain}/dns",
            f"https://viewdns.info/dnsrecord/?domain={target.domain}",
        ],
    }
