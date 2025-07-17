# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-07-17

### Added
- **Table of Contents (TOC) generation**: New `--toc` flag automatically generates navigation from h1/h2/h3 headers
  - Scans markdown headers and creates anchor links
  - Assigns unique IDs to headers for navigation
  - Places TOC as the first element in document body
- **Theme support**: New `--theme [light|dark]` option for built-in styling
  - Light theme (default): White background (#fff), black text (#000)
  - Dark theme: Dark background (#181818), light text (#e9e9e9), blue links (#9cccff)
  - CSS styles embedded directly in HTML output
- **Enhanced HTML output**: Full HTML document structure with DOCTYPE, head, and body tags
- **Comprehensive test suite**: Added 3 new tests for TOC and theme functionality

### Changed
- Updated `convert_markdown_to_html()` function to support new features
- Enhanced CLI argument parsing with new options
- Improved HTML structure with proper document formatting

### Technical Details
- Added `beautifulsoup4` dependency for HTML manipulation
- Implemented `get_theme_css()`, `generate_header_id()`, and `build_toc()` functions
- Maintained backward compatibility with existing CLI usage
- All tests passing (7/7) with Python 3.10+ compatibility

## [1.0.0] - Initial Release

### Added
- Basic Markdown to HTML conversion using `markdown` package
- CLI interface: `python md2html.py <file.md>`
- Error handling for non-existent files
- Unit tests with pytest
- README documentation
