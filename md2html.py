#!/usr/bin/env python3
"""
md2html - Convert Markdown files to HTML
"""
import sys
import argparse
import re
import markdown
from bs4 import BeautifulSoup


def get_theme_css(theme):
    """Get CSS styles for the specified theme."""
    if theme == "dark":
        return """
body { background:#181818; color:#e9e9e9; font-family: Arial, sans-serif; }
a { color:#9cccff; }
nav { margin-bottom: 2em; }
nav ul { list-style-type: none; padding-left: 0; }
nav li { margin: 0.5em 0; }
"""
    else:  # light theme (default)
        return """
body { background:#fff; color:#000; font-family: Arial, sans-serif; }
a { color:#0066cc; }
nav { margin-bottom: 2em; }
nav ul { list-style-type: none; padding-left: 0; }
nav li { margin: 0.5em 0; }
"""


def generate_header_id(text):
    """Generate a URL-friendly ID from header text."""
    header_id = re.sub(r"[^\w\s-]", "", text.lower())
    header_id = re.sub(r"[-\s]+", "-", header_id)
    return header_id.strip("-")


def build_toc(soup):
    """Build table of contents from h1, h2, h3 headers."""
    headers = soup.find_all(["h1", "h2", "h3"])
    if not headers:
        return None

    toc_items = []
    for header in headers:
        text = header.get_text()
        header_id = generate_header_id(text)
        header["id"] = header_id

        level = int(header.name[1])  # Extract number from h1, h2, h3
        toc_items.append({"text": text, "id": header_id, "level": level})

    nav = soup.new_tag("nav")
    ul = soup.new_tag("ul")

    for item in toc_items:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=f"#{item['id']}")
        a.string = item["text"]
        li.append(a)
        ul.append(li)

    nav.append(ul)
    return nav


def convert_markdown_to_html(markdown_content, add_toc=False, theme="light"):
    """Convert markdown content to HTML with optional TOC and theme."""
    md = markdown.Markdown()
    html_content = md.convert(markdown_content)

    soup = BeautifulSoup(html_content, "html.parser")

    html_doc = BeautifulSoup(
        "<!DOCTYPE html><html><head></head><body></body></html>", "html.parser"
    )

    style_tag = html_doc.new_tag("style")
    style_tag.string = get_theme_css(theme)
    html_doc.head.append(style_tag)

    if add_toc:
        for element in soup.contents:
            if element.name:  # Skip text nodes
                html_doc.body.append(element.extract())

        toc = build_toc(html_doc)
        if toc:
            html_doc.body.insert(0, toc)
    else:
        for element in soup.contents:
            if element.name:  # Skip text nodes
                html_doc.body.append(element.extract())

    return str(html_doc)


def main():
    """Main CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Convert Markdown files to HTML")
    parser.add_argument("file", help="Markdown file to convert")
    parser.add_argument(
        "--toc", action="store_true", help="Generate table of contents from headers"
    )
    parser.add_argument(
        "--theme",
        choices=["light", "dark"],
        default="light",
        help="Theme for HTML output (default: light)",
    )

    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        html_output = convert_markdown_to_html(
            markdown_content, add_toc=args.toc, theme=args.theme
        )
        print(html_output)

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
