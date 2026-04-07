#!/usr/bin/env python3
"""
WordPress XML → Hugo Markdown converter.

Usage:
  python3 tools/wp_to_hugo.py --dry-run   # 測試模式，只顯示不寫檔
  python3 tools/wp_to_hugo.py             # 全量轉換
"""
import argparse
import html
import os
import re
import sys
import urllib.parse
from datetime import datetime

import yaml
from lxml import etree
from markdownify import markdownify as md

# ── 路徑設定 ──────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML_PATH = os.path.join(BASE_DIR, "tools", "josh039snotebook.WordPress.2026-04-07.xml")
OUTPUT_DIR = os.path.join(BASE_DIR, "content", "posts")

# ── 命名空間 ──────────────────────────────────────────────
WP_NS = "http://wordpress.org/export/1.2/"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
DC_NS = "http://purl.org/dc/elements/1.1/"


def decode_slug(raw_slug: str) -> str:
    """URL-decode a WordPress slug and normalise it."""
    try:
        decoded = urllib.parse.unquote(raw_slug)
    except Exception:
        decoded = raw_slug
    # keep lowercase and replace spaces with hyphens
    decoded = decoded.strip().lower().replace(" ", "-")
    # remove characters that are not alphanumeric, hyphens, or Chinese/Japanese/Korean
    decoded = re.sub(r"[^\w\-\u3000-\u9fff\uff00-\uffef]", "-", decoded, flags=re.UNICODE)
    decoded = re.sub(r"-{2,}", "-", decoded).strip("-")
    return decoded or "untitled"


def rewrite_image_urls(html_content: str) -> str:
    """Rewrite WordPress CDN image URLs to local /images/[year]/[filename]."""
    pattern = re.compile(
        r'(https?://[^"\'>\s]+\.wordpress\.com/wp-content/uploads/(\d{4})/\d{2}/([^"\'>\s]+))',
        re.IGNORECASE,
    )

    def replace(m):
        year = m.group(2)
        filename = m.group(3).split("?")[0]  # strip query string
        return f"/images/{year}/{filename}"

    return pattern.sub(replace, html_content)


def html_to_markdown(raw_html: str) -> str:
    """Convert HTML content to Markdown, rewriting image URLs first."""
    if not raw_html:
        return ""
    # unescape HTML entities (WordPress sometimes double-encodes)
    content = html.unescape(raw_html)
    # rewrite image URLs before conversion
    content = rewrite_image_urls(content)
    # convert to markdown
    result = md(
        content,
        heading_style="ATX",
        bullets="-",
        code_language_callback=lambda el: el.get("class", [""])[0].replace("language-", "") if el.get("class") else "",
        strip=["script", "style"],
        newline_style="backslash",
    )
    # clean up excessive blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def make_front_matter(title: str, date: str, slug: str,
                       tags: list, categories: list) -> str:
    """Return YAML front matter block."""
    data = {
        "title": title,
        "date": date,
        "slug": slug,
        "tags": tags,
        "categories": categories,
        "draft": False,
    }
    return "---\n" + yaml.dump(data, allow_unicode=True, default_flow_style=False) + "---\n"


def safe_filename(slug: str, post_id: str) -> str:
    """Return a filesystem-safe filename from slug."""
    name = slug if slug else f"post-{post_id}"
    # keep only safe chars
    name = re.sub(r"[^\w\-]", "-", name, flags=re.UNICODE)
    name = re.sub(r"-{2,}", "-", name).strip("-")
    return (name or f"post-{post_id}") + ".md"


def convert(dry_run: bool = False):
    with open(XML_PATH, "rb") as f:
        tree = etree.parse(f)
    root = tree.getroot()
    channel = root.find("channel")

    if not dry_run:
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    success = 0
    skipped = 0
    errors = []

    for item in channel.findall("item"):
        try:
            post_type = item.findtext(f"{{{WP_NS}}}post_type", "")
            if post_type != "post":
                continue

            status = item.findtext(f"{{{WP_NS}}}status", "")
            if status != "publish":
                skipped += 1
                continue

            title = item.findtext("title", "").strip()
            title = html.unescape(title)

            raw_date = item.findtext(f"{{{WP_NS}}}post_date", "")
            try:
                dt = datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")
                date_str = dt.strftime("%Y-%m-%dT%H:%M:%S+08:00")
            except ValueError:
                date_str = raw_date

            raw_slug = item.findtext(f"{{{WP_NS}}}post_name", "")
            slug = decode_slug(raw_slug)
            post_id = item.findtext(f"{{{WP_NS}}}post_id", "0")

            tags = []
            categories = []
            for cat_elem in item.findall("category"):
                domain = cat_elem.get("domain", "")
                text = (cat_elem.text or "").strip()
                if domain == "post_tag" and text:
                    tags.append(text)
                elif domain == "category" and text and text != "Uncategorized":
                    categories.append(text)

            # get post content
            content_elem = item.find(f"{{{CONTENT_NS}}}encoded")
            raw_content = content_elem.text if content_elem is not None and content_elem.text else ""

            body_md = html_to_markdown(raw_content)
            front_matter = make_front_matter(title, date_str, slug, tags, categories)
            full_content = front_matter + "\n" + body_md + "\n"

            filename = safe_filename(slug, post_id)
            out_path = os.path.join(OUTPUT_DIR, filename)

            if dry_run:
                print(f"[DRY-RUN] Would write: content/posts/{filename}")
                print(f"          Title: {title}")
                print(f"          Date:  {date_str}")
                print(f"          Tags:  {tags}  Categories: {categories}")
                print()
            else:
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(full_content)
                print(f"  ✓ {filename}")

            success += 1

        except Exception as e:
            err_msg = f"ERROR processing item '{item.findtext('title', 'unknown')}': {e}"
            print(err_msg, file=sys.stderr)
            errors.append(err_msg)

    mode = "[DRY-RUN]" if dry_run else "[DONE]"
    print(f"\n{mode} 轉換成功: {success} 篇 | 跳過草稿: {skipped} 篇 | 錯誤: {len(errors)} 篇")
    if errors:
        print("\n錯誤清單:")
        for e in errors:
            print(f"  {e}")

    return success, skipped, errors


def main():
    parser = argparse.ArgumentParser(description="WordPress XML → Hugo Markdown")
    parser.add_argument("--dry-run", action="store_true", help="測試模式，不寫入檔案")
    args = parser.parse_args()
    convert(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
