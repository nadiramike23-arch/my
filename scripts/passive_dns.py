#!/usr/bin/env python3
"""passive_dns.py - simple passive DNS wrapper (requires an API key)

This script does not include a built-in integration by default. Many passive-DNS providers exist (SecurityTrails, VirusTotal, PassiveTotal, etc.).
Set PASSIVE_DNS_PROVIDER and PASSIVE_DNS_KEY environment variables and adapt the small provider blocks below.

Usage examples (example only):
  export PASSIVE_DNS_PROVIDER=securitytrails
  export PASSIVE_DNS_KEY="..."
  python scripts/passive_dns.py example.com

Requires: requests
"""
import argparse
import os
import sys
import requests

PROVIDERS = ("securitytrails", "virustotal", "passivetotal")


def query_securitytrails(domain, key):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/history"  # illustrative
    headers = {"APIKEY": key}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json()


def main():
    p = argparse.ArgumentParser(description="Passive DNS lookup (provider wrapper)")
    p.add_argument("domain")
    args = p.parse_args()

    provider = os.getenv("PASSIVE_DNS_PROVIDER")
    key = os.getenv("PASSIVE_DNS_KEY")

    if not provider or not key:
        print("PASSIVE_DNS_PROVIDER and PASSIVE_DNS_KEY must be set in the environment.\n")
        print("Supported (example) providers:", ", ".join(PROVIDERS))
        sys.exit(2)

    provider = provider.lower()
    try:
        if provider == "securitytrails":
            data = query_securitytrails(args.domain, key)
        else:
            raise NotImplementedError(f"Provider integration not implemented: {provider}")
    except Exception as e:
        print("Error querying provider:", e)
        sys.exit(1)

    import json
    print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
