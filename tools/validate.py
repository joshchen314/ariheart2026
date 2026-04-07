#!/usr/bin/env python3
"""
Validate Hugo Markdown front matter completeness.

Checks all .md files under content/ for required front matter fields.
Outputs a report to tools/validation_report.txt.
"""
import os
import re
import sys

import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
REPORT_PATH = os.path.join(BASE_DIR, "tools", "validation_report.txt")

REQUIRED_FIELDS = ["title", "date", "draft"]
POSTS_REQUIRED = ["title", "date", "slug", "draft"]

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_front_matter(filepath):
    """Return (front_matter_dict, errors) for a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = FRONT_MATTER_RE.match(content)
    if not m:
        return None, ["missing front matter block"]

    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, [f"YAML parse error: {e}"]

    if not isinstance(fm, dict):
        return {}, ["front matter is not a dict"]

    return fm, []


def validate_file(filepath):
    """Return list of issue strings (empty = OK)."""
    rel = os.path.relpath(filepath, BASE_DIR)
    is_post = "content/posts" in rel.replace("\\", "/")

    fm, errors = parse_front_matter(filepath)
    if errors:
        return errors

    required = POSTS_REQUIRED if is_post else REQUIRED_FIELDS
    for field in required:
        if field not in fm:
            errors.append(f"missing field: '{field}'")

    if "title" in fm and not fm["title"]:
        errors.append("title is empty")

    if "date" in fm and not fm["date"]:
        errors.append("date is empty")

    return errors


def main():
    issues = {}
    ok_count = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        # skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            errs = validate_file(fpath)
            rel = os.path.relpath(fpath, BASE_DIR)
            if errs:
                issues[rel] = errs
            else:
                ok_count += 1

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("=== Hugo Front Matter Validation Report ===\n\n")
        f.write(f"OK: {ok_count} 個檔案\n")
        f.write(f"問題: {len(issues)} 個檔案\n\n")

        if issues:
            f.write("=== 問題清單 ===\n")
            for path, errs in sorted(issues.items()):
                f.write(f"\n{path}:\n")
                for e in errs:
                    f.write(f"  - {e}\n")
        else:
            f.write("所有檔案通過驗證！\n")

    print(f"驗證完成: {ok_count} OK, {len(issues)} 個問題")
    print(f"報告: {REPORT_PATH}")

    if issues:
        print("\n問題清單:")
        for path, errs in sorted(issues.items()):
            print(f"  {path}: {', '.join(errs)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
