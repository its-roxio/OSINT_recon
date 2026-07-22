import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

MAX_URLS = 50


def run(target):
    start_url = f"{target.scheme}://{target.domain}:{target.port}{target.path}"
    visited = {start_url}
    to_visit = [start_url]
    internal = []
    external = []

    while to_visit and len(visited) < MAX_URLS:
        url = to_visit.pop(0)
        try:
            resp = requests.get(url, timeout=10)
        except Exception:
            continue

        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = urljoin(url, a["href"])
            if href in visited:
                continue
            visited.add(href)

            parsed = urlparse(href)
            if parsed.hostname == target.domain:
                internal.append(href)
                to_visit.append(href)
            else:
                external.append(href)

    robots = f"{target.scheme}://{target.domain}/robots.txt"
    sitemap = f"{target.scheme}://{target.domain}/sitemap.xml"

    return {
        "start_url": start_url,
        "internal_links": internal,
        "external_links": external,
        "robots": robots,
        "sitemap": sitemap,
        "references": [
            f"https://www.google.com/search?q=site:{target.domain}",
            f"https://yandex.ru/search/?text=site:{target.domain}",
        ],
    }
