# md2html

A Python CLI tool to convert Markdown files to HTML with table of contents and theme support.

## Features

- Convert Markdown to HTML using the `markdown` package
- Generate Table of Contents (TOC) from headers with `--toc` flag
- Apply light/dark themes with `--theme [light|dark]` option
- Full HTML document output with proper structure

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic conversion
```bash
python md2html.py example.md
```

### With Table of Contents
```bash
python md2html.py --toc example.md
```

### With dark theme
```bash
python md2html.py --theme dark example.md
```

### Combined options
```bash
python md2html.py --toc --theme dark example.md
```

## Options

- `--toc`: Generate table of contents from H1/H2/H3 headers
- `--theme [light|dark]`: Apply built-in CSS theme (default: light)

## Theme Details

### Light Theme (default)
- Background: White (#fff)
- Text: Black (#000)

### Dark Theme
- Background: Dark gray (#181818)
- Text: Light gray (#e9e9e9)
- Links: Light blue (#9cccff)

## Example Output

With `--toc --theme dark`, a markdown file with headers will generate:
- Full HTML document structure
- Navigation menu with anchor links
- Dark theme styling
- Responsive design

## Development

### Running Tests
```bash
pytest -v
```

### Code Quality
```bash
ruff .
black .
```

## Project Structure

```
md2html/
├── md2html.py          # Main CLI script
├── tests/
│   └── test_md2html.py # Unit tests
├── requirements.txt    # Dependencies
├── pyproject.toml     # Project metadata
├── CHANGELOG.md       # Version history
└── README.md          # This file
```

⚡️ Ruff auto-fix CI 테스트
