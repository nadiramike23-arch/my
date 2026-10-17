#!/usr/bin/env python3
"""subdomain_enum.py - naive subdomain enumeration using a wordlist and DNS resolution

Usage: python scripts/subdomain_enum.py example.com --wordlist data/subdomains.txt

Requires: dnspython (pip install dnspython)
"""
import argparse
import dns.resolver
import sys


def resolve(name):
    try:
        answers = dns.resolver.resolve(name, "A")
        return [r.to_text() for r in answers]
    except Exception:
        return []


def main():
    p = argparse.ArgumentParser(description="Naive subdomain enumeration")
    p.add_argument("domain", help="Target domain (e.g. example.com)")
    p.add_argument("--wordlist", default="data/subdomains.txt", help="Path to wordlist")
    args = p.parse_args()

    try:
        with open(args.wordlist, "r") as f:
            words = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    except FileNotFoundError:
        print(f"Wordlist not found: {args.wordlist}")
        sys.exit(2)

    for w in words:
        name = f"{w}.{args.domain}"
        ips = resolve(name)
        if ips:
            print(f"FOUND: {name} -> {', '.join(ips)}")


if __name__ == "__main__":
    main()
