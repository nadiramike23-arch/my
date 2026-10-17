#!/usr/bin/env python3
"""screenshot_wrapper.py - minimal page snapshotter

Attempts to use Playwright (recommended) if installed. Falls back to fetching HTML via requests and saving it.

Usage: python scripts/screenshot_wrapper.py https://example.com output.png

Requirements (optional): playwright (pip install playwright) and `playwright install` to download browsers
"""
import argparse
import sys
import os


def save_html(url, out):
    import requests
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    with open(out, "w", encoding="utf-8") as f:
        f.write(r.text)


def screenshot_playwright(url, out):
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        raise
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=30000)
        page.screenshot(path=out, full_page=True)
        browser.close()


def main():
    p = argparse.ArgumentParser(description="Page snapshotter: screenshot (png) or HTML fallback")
    p.add_argument("url")
    p.add_argument("output", help="Output file path (png for screenshot or .html for HTML)")
    args = p.parse_args()

    out = args.output
    try:
        if out.lower().endswith(".png"):
            try:
                screenshot_playwright(args.url, out)
                print(f"Screenshot saved to {out}")
                return
            except Exception:
                print("Playwright not available or failed; falling back to HTML save.")
                save_html(args.url, out.replace('.png', '.html'))
                print(f"Saved HTML fallback to {out.replace('.png', '.html')}")
        else:
            save_html(args.url, out)
            print(f"Saved HTML to {out}")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
