import argparse
from .core.target import Target
from .modules import (
    headers,
    whois_dns,
    ssl_cert,
    tech_stack,
    crawl,
    subdomains,
    ports_traceroute,
    wayback_dirs,
    org_intel,
)
from .export import report as report_export


def build_parser():
    parser = argparse.ArgumentParser(description="OSINT web recon tool")
    parser.add_argument("--url", required=True, help="Target URL or domain")
    parser.add_argument("--full", action="store_true", help="Run full reconnaissance")
    parser.add_argument("--headers", action="store_true", help="HTTP headers")
    parser.add_argument("--whois", action="store_true", help="WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="DNS records")
    parser.add_argument("--ssl", action="store_true", help="SSL certificate")
    parser.add_argument("--tech", action="store_true", help="Tech stack analysis")
    parser.add_argument("--crawl", action="store_true", help="Basic crawler")
    parser.add_argument("--sub", action="store_true", help="Subdomain discovery")
    parser.add_argument("--ports", action="store_true", help="Common port scan")
    parser.add_argument("--trace", action="store_true", help="Traceroute (placeholder)")
    parser.add_argument("--wayback", action="store_true", help="Wayback directories")
    parser.add_argument("--org", action="store_true", help="Organisation & people OSINT")
    parser.add_argument("--export", choices=["json", "md"], default="json", help="Report format")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    target = Target(args.url)
    report = {"target": target.to_dict()}

    def run_if(flag_name, func, key):
        if args.full or getattr(args, flag_name):
            report[key] = func(target)

    run_if("headers", headers.run, "headers")
    run_if("whois", whois_dns.run_whois, "whois")
    run_if("dns", whois_dns.run_dns, "dns")
    run_if("ssl", ssl_cert.run, "ssl")
    run_if("tech", tech_stack.run, "tech_stack")
    run_if("crawl", crawl.run, "crawl")
    run_if("sub", subdomains.run, "subdomains")
    run_if("ports", ports_traceroute.run_ports, "ports")
    run_if("trace", ports_traceroute.run_trace, "traceroute")
    run_if("wayback", wayback_dirs.run, "wayback")
    run_if("org", org_intel.run, "organisation")

    report_export.export(report, fmt=args.export)


if __name__ == "__main__":
    main()
