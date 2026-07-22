import requests
from bs4 import BeautifulSoup


def run(target):
    url = f"{target.scheme}://{target.domain}:{target.port}{target.path}"
    try:
        resp = requests.get(url, timeout=10)
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(resp.text, "html.parser")

    meta_gen = [m.get("content") for m in soup.find_all("meta", attrs={"name": "generator"})]
    scripts = [s.get("src") for s in soup.find_all("script") if s.get("src")]
    links = [l.get("href") for l in soup.find_all("link") if l.get("href")]

    detected = {
        "meta_generator": meta_gen,
        "scripts": scripts,
        "links": links,
    }

    return {
        "url": url,
        "detected": detected,
        "references": [
            f"https://builtwith.com/{target.domain}",
            f"https://www.wappalyzer.com/lookup/{target.domain}",
        ],
    }
