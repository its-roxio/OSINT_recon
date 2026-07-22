def run(target):
    domain = target.domain

    dorks = [
        f'site:{domain} filetype:pdf',
        f'site:{domain} filetype:docx',
        f'site:{domain} filetype:xlsx',
        f'site:{domain} intext:"@{domain}"',
        f'"@{domain}" -site:{domain}',
        f'site:{domain} inurl:(contact OR about OR team)',
    ]

    return {
        "domain": domain,
        "dorks": dorks,
        "references": [
            f"https://www.google.com/search?q=site:{domain}+filetype:pdf",
            f"https://duckduckgo.com/?q=site%3A{domain}+filetype%3Apdf",
        ],
    }
