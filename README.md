# Cyber Detective — OSINT Toolkit

Cyber Detective is a beginner-friendly OSINT (Open-Source Intelligence) toolkit and learning project. It provides small, documented utilities, playbooks, and examples to perform safe, legal, and ethical OSINT investigations for learning, red-teaming planning, or defensive threat intelligence.

Features
- Simple command-line OSINT utilities: domain lookup, WHOIS, passive DNS, subdomain enumeration, basic screenshotting using services or headless browsers.
- Example data collectors and parsers (JSON output) for easy pipeline integration.
- Investigation playbook and checklist to run safe and repeatable inquiries.
- Jupyter notebooks with examples of timeline building and entity correlation.
- Guidance on ethics, legality, and operational safety.

Quick start
1. Clone the repository:
   git clone https://github.com/nadiramike23-arch/my.git
   cd my
2. Create a virtual environment and install dependencies (Python 3.10+ recommended):
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

Usage examples
- Lookup WHOIS information for a domain:
  python scripts/whois_lookup.py example.com

- Enumerate common subdomains from a wordlist:
  python scripts/subdomain_enum.py example.com --wordlist data/subdomains.txt

- Run passive DNS query (requires API key in env):
  export PASSIVE_DNS_KEY="..."
  python scripts/passive_dns.py example.com

Project layout
- scripts/ — small CLI utilities (whois, subdomain enumeration, passive DNS wrapper, screenshotter)
- data/ — small sample datasets and wordlists (safe, non-sensitive examples)
- notebooks/ — Jupyter notebooks for analysis and timeline building
- docs/ — playbook, investigation checklist, and ethics guide
- requirements.txt — Python dependencies

Security, ethics, and legal guidance
- Always follow your local laws and the terms of service of any third-party services. OSINT investigations can cross legal boundaries — do not access systems you do not own or have explicit permission to test.
- Prefer passive techniques (public records, DNS, WHOIS, archives) and avoid active scanning that could be construed as intrusion.
- When storing findings, redact personal data not required for the investigation and follow data-retention best practices.
- Use this repo for learning and defensive research only unless you have explicit written authorization to do more.

Investigation playbook (high-level)
1. Define scope and objectives — what question are you trying to answer?
2. Identify permitted data sources and get any necessary approvals.
3. Collect passive data (WHOIS, DNS, archived pages, certificate transparency logs, social profiles).
4. Normalize and enrich data (timestamps, IP resolution, geo, ASN, related domains).
5. Correlate entities to build a timeline or map.
6. Document steps, findings, and sources. Maintain reproducible scripts.
7. Close out: archive collected data, redact sensitive information, and record retention/destruction schedule.

Contributing
- Issues and PRs welcome. Label bugfixes and feature requests clearly.
- Add tests and documentation for new scripts.
- When adding integrations that require API keys, use environment variables and do not check secrets into the repository.

Examples and resources
- Example notebooks show how to build a simple timeline from archived web pages and DNS resolution history.
- Links to public OSINT resources and reading materials are included in docs/RESOURCES.md.

License
- MIT

Acknowledgements
- Built for learning and defensive research. Use responsibly.
