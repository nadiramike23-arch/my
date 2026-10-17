# Investigation Playbook (detailed)

This playbook expands the high-level steps in the README into practical actions for small OSINT inquiries.

1) Define scope
- List targets (domains, handles) and the research question
- Record permitted actions and any approvals

2) Passive collection
- WHOIS / RDAP lookups
- Passive DNS queries and historical resolution
- Certificate Transparency (crt.sh) searches for related domains/subdomains
- Wayback Machine / archive snapshots
- Public social media profiles and public registries

3) Enrichment
- Resolve IPs, map to ASNs, and geo-locate
- Use threat intelligence sources to enrich indicators (VT, AbuseIPDB)
- Collate timestamps and normalize to UTC

4) Correlation and analysis
- Build entity relationships (domains -> IPs -> certificates -> registrars)
- Construct timelines from archived pages and DNS history

5) Reporting and documentation
- Document data sources and commands used
- Redact unnecessary personal data
- Store artifacts and define retention

6) Cleanup
- Revoke any API keys used on testing infra; rotate credentials if needed

