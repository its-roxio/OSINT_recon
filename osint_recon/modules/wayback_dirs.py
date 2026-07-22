import requests


def run(target):
    url = f"http://web.archive.org/cdx/search/cdx?url={target.domain}/*&output=json&limit=50"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
    except Exception as e:
        return {"error": str(e)}

    paths = sorted({row[2] for row in data[1:] if len(row) > 2})

    return {
        "paths": paths,
        "references": [
            f"https://web.archive.org/web/*/{target.domain}",
            f"https://archive.today/{target.domain}",
        ],
    }
