#!/usr/bin/env python3
"""Analyze WordPress XML export and generate audit report + taxonomy map."""
import json
import os
from collections import Counter
from lxml import etree

XML_PATH = os.path.join(os.path.dirname(__file__), "josh039snotebook.WordPress.2026-04-07.xml")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "audit_report.txt")
TAXONOMY_PATH = os.path.join(os.path.dirname(__file__), "taxonomy_map.json")

WP_NS = "http://wordpress.org/export/1.2/"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
DC_NS = "http://purl.org/dc/elements/1.1/"


def parse_xml(path):
    with open(path, "rb") as f:
        tree = etree.parse(f)
    return tree.getroot()


def main():
    root = parse_xml(XML_PATH)
    channel = root.find("channel")

    posts = []
    pages = []
    attachments = []
    tags = Counter()
    categories = Counter()
    image_urls = []

    for item in channel.findall("item"):
        post_type = item.findtext(f"{{{WP_NS}}}post_type", "")
        status = item.findtext(f"{{{WP_NS}}}status", "")

        if post_type == "post":
            posts.append({
                "title": item.findtext("title", ""),
                "status": status,
                "slug": item.findtext(f"{{{WP_NS}}}post_name", ""),
                "date": item.findtext(f"{{{WP_NS}}}post_date", ""),
            })
        elif post_type == "page":
            pages.append({
                "title": item.findtext("title", ""),
                "status": status,
                "slug": item.findtext(f"{{{WP_NS}}}post_name", ""),
            })
        elif post_type == "attachment":
            url = item.findtext(f"{{{WP_NS}}}attachment_url", "")
            if url:
                attachments.append(url)
                if any(url.lower().endswith(ext) for ext in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg")):
                    image_urls.append(url)

        # tags and categories
        for cat_elem in item.findall("category"):
            domain = cat_elem.get("domain", "")
            nicename = cat_elem.get("nicename", "")
            text = (cat_elem.text or "").strip()
            if domain == "post_tag":
                tags[text] += 1
            elif domain == "category":
                categories[text] += 1

    published_posts = [p for p in posts if p["status"] == "publish"]
    draft_posts = [p for p in posts if p["status"] != "publish"]

    # Write audit report
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("=== WordPress XML Audit Report ===\n\n")
        f.write(f"文章 (post) 總數: {len(posts)}\n")
        f.write(f"  - 已發布: {len(published_posts)}\n")
        f.write(f"  - 草稿/其他: {len(draft_posts)}\n")
        f.write(f"頁面 (page) 總數: {len(pages)}\n")
        f.write(f"附件 (attachment) 總數: {len(attachments)}\n")
        f.write(f"圖片檔案數量: {len(image_urls)}\n\n")

        f.write("=== 標籤 (Tags) ===\n")
        for tag, count in tags.most_common():
            f.write(f"  {tag}: {count} 篇\n")

        f.write("\n=== 分類 (Categories) ===\n")
        for cat, count in categories.most_common():
            f.write(f"  {cat}: {count} 篇\n")

        f.write("\n=== 已發布文章列表 ===\n")
        for p in published_posts:
            f.write(f"  [{p['date'][:10]}] {p['title']} (slug: {p['slug']})\n")

        f.write("\n=== 圖片 URL 清單 ===\n")
        for url in image_urls:
            f.write(f"  {url}\n")

    print(f"審計報告已寫入: {REPORT_PATH}")

    # Build taxonomy map
    taxonomy_map = {
        "tags": {tag: {"hugo_taxonomy": "tags", "slug": tag.lower().replace(" ", "-")} for tag in tags},
        "categories": {cat: {"hugo_taxonomy": "categories", "slug": cat.lower().replace(" ", "-")} for cat in categories},
    }

    with open(TAXONOMY_PATH, "w", encoding="utf-8") as f:
        json.dump(taxonomy_map, f, ensure_ascii=False, indent=2)

    print(f"Taxonomy map 已寫入: {TAXONOMY_PATH}")

    # Print summary
    print(f"\n=== 摘要 ===")
    print(f"文章總數: {len(posts)} (已發布: {len(published_posts)}, 草稿: {len(draft_posts)})")
    print(f"頁面總數: {len(pages)}")
    print(f"圖片數量: {len(image_urls)}")
    print(f"標籤數量: {len(tags)}")
    print(f"分類數量: {len(categories)}")

    return {
        "posts": len(posts),
        "published_posts": len(published_posts),
        "pages": len(pages),
        "images": len(image_urls),
        "tags": list(tags.keys()),
        "categories": list(categories.keys()),
    }


if __name__ == "__main__":
    main()
