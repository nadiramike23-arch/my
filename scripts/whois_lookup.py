#!/usr/bin/env python3
"""whois_lookup.py - simple WHOIS lookup utility

Usage: python scripts/whois_lookup.py example.com

Requires: python-whois (pip install python-whois)
"""
import argparse
import json
import sys

try:
    import whois
except Exception:
    print("Missing dependency: python-whois. Install with `pip install python-whois`.")
    sys.exit(2)


def lookup(domain: str) -> dict:
    return whois.whois(domain)


def main():
    p = argparse.ArgumentParser(description="Simple WHOIS lookup")
    p.add_argument("domain", help="Domain to query")
    args = p.parse_args()

    result = lookup(args.domain)
    # whois.whois returns a dict-like object; convert to JSON-serializable form
    out = {k: (list(v) if isinstance(v, set) else v) for k, v in dict(result).items()}
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
