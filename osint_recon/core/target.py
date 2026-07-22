from urllib.parse import urlparse
import socket


class Target:
    def __init__(self, url: str):
        self.raw = url
        parsed = urlparse(url if "://" in url else "http://" + url)
        self.scheme = parsed.scheme or "http"
        self.domain = parsed.hostname
        self.port = parsed.port or (443 if self.scheme == "https" else 80)
        self.path = parsed.path or "/"
        self.ip = self._resolve_ip(self.domain)

    def _resolve_ip(self, domain: str):
        try:
            return socket.gethostbyname(domain)
        except Exception:
            return None

    def to_dict(self):
        return {
            "raw": self.raw,
            "scheme": self.scheme,
            "domain": self.domain,
            "port": self.port,
            "path": self.path,
            "ip": self.ip,
        }
