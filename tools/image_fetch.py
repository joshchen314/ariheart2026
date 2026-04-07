#!/usr/bin/env python3
"""
Download all images from WordPress XML export.

- Downloads to static/images/[year]/[filename]
- Skips existing files
- Records failures to tools/image_errors.txt
"""
import os
import re
import sys
import time
import urllib.parse

import requests
from lxml import etree

# ── Paths ─────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML_PATH = os.path.join(BASE_DIR, "tools", "josh039snotebook.WordPress.2026-04-07.xml")
STATIC_DIR = os.path.join(BASE_DIR, "static", "images")
ERROR_LOG = os.path.join(BASE_DIR, "tools", "image_errors.txt")

WP_NS = "http://wordpress.org/export/1.2/"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"

IMAGE_PATTERN = re.compile(
    r"https?://[^\s\"'<>]+\.wordpress\.com/wp-content/uploads/(\d{4})/\d{2}/([^\s\"'<>?#]+)",
    re.IGNORECASE,
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ariheart-importer/1.0)",
}


def collect_image_urls(root):
    """Collect all unique image URLs from the XML."""
    urls = {}  # url → (year, filename)
    channel = root.find("channel")
    if channel is None:
        return urls

    for item in channel.findall("item"):
        # attachment_url
        att_url = item.findtext(f"{{{WP_NS}}}attachment_url", "")
        if att_url:
            m = IMAGE_PATTERN.search(att_url)
            if m:
                urls[att_url] = (m.group(1), m.group(2).split("?")[0])

        # content:encoded
        content_elem = item.find(f"{{{CONTENT_NS}}}encoded")
        raw = content_elem.text if content_elem is not None and content_elem.text else ""
        for m in IMAGE_PATTERN.finditer(raw):
            url = m.group(0).split("?")[0]
            urls[url] = (m.group(1), m.group(2).split("?")[0])

    return urls


def download(url, dest_path):
    """Download url to dest_path. Returns True on success."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        resp.raise_for_status()
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as f:
            for chunk in resp.iter_content(8192):
                f.write(chunk)
        return True
    except Exception as e:
        return str(e)


def main():
    with open(XML_PATH, "rb") as f:
        root = etree.parse(f).getroot()

    urls = collect_image_urls(root)
    print(f"找到 {len(urls)} 個圖片 URL")

    errors = []
    downloaded = 0
    skipped = 0

    for url, (year, filename) in urls.items():
        dest = os.path.join(STATIC_DIR, year, filename)
        if os.path.exists(dest):
            print(f"  [SKIP] {year}/{filename}")
            skipped += 1
            continue

        result = download(url, dest)
        if result is True:
            size = os.path.getsize(dest)
            print(f"  [OK]   {year}/{filename}  ({size:,} bytes)")
            downloaded += 1
        else:
            print(f"  [ERR]  {url}: {result}", file=sys.stderr)
            errors.append(f"{url}: {result}")

        time.sleep(0.5)  # be polite

    # write error log
    with open(ERROR_LOG, "w", encoding="utf-8") as f:
        if errors:
            f.write("\n".join(errors) + "\n")
        else:
            f.write("(no errors)\n")

    print(f"\n完成: 下載 {downloaded} 張 | 跳過 {skipped} 張 | 錯誤 {len(errors)} 張")
    print(f"錯誤記錄: {ERROR_LOG}")


if __name__ == "__main__":
    main()
