"""
Tests for md2html module
"""

import pytest
import tempfile
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from md2html import convert_markdown_to_html, main


def test_convert_simple_markdown():
    """Test converting simple markdown to HTML."""
    markdown_content = "# Hello World\n\nThis is a **bold** text."

    result = convert_markdown_to_html(markdown_content)
    assert "<h1>Hello World</h1>" in result
    assert "<p>This is a <strong>bold</strong> text.</p>" in result
    assert "<!DOCTYPE html>" in result
    assert "<style>" in result


def test_convert_markdown_with_list():
    """Test converting markdown with list to HTML."""
    markdown_content = "## Items\n\n- Item 1\n- Item 2\n- Item 3"
    result = convert_markdown_to_html(markdown_content)

    assert "<h2>Items</h2>" in result
    assert "<ul>" in result
    assert "<li>Item 1</li>" in result
    assert "<li>Item 2</li>" in result
    assert "<li>Item 3</li>" in result


def test_main_with_valid_file(capsys):
    """Test main function with a valid markdown file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("# Test\n\nThis is a test.")
        temp_file = f.name

    try:
        original_argv = sys.argv
        sys.argv = ["md2html.py", temp_file]

        main()

        captured = capsys.readouterr()
        assert "<h1>Test</h1>" in captured.out
        assert "<p>This is a test.</p>" in captured.out

    finally:
        sys.argv = original_argv
        os.unlink(temp_file)


def test_main_with_nonexistent_file(capsys):
    """Test main function with a non-existent file."""
    original_argv = sys.argv
    sys.argv = ["md2html.py", "nonexistent.md"]

    try:
        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "Error: File 'nonexistent.md' not found." in captured.err

    finally:
        sys.argv = original_argv


def test_toc_generation(capsys):
    """Test TOC generation with --toc flag."""
    markdown_content = "# Main Title\n\nSome content.\n\n## Subtitle\n\nMore content."

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(markdown_content)
        temp_file = f.name

    try:
        original_argv = sys.argv
        sys.argv = ["md2html.py", "--toc", temp_file]

        main()

        captured = capsys.readouterr()
        assert "<nav>" in captured.out
        assert 'href="#main-title"' in captured.out
        assert 'href="#subtitle"' in captured.out
        assert 'id="main-title"' in captured.out
        assert 'id="subtitle"' in captured.out

    finally:
        sys.argv = original_argv
        os.unlink(temp_file)


def test_dark_theme(capsys):
    """Test dark theme application with --theme dark."""
    markdown_content = "# Test\n\nContent."

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(markdown_content)
        temp_file = f.name

    try:
        original_argv = sys.argv
        sys.argv = ["md2html.py", "--theme", "dark", temp_file]

        main()

        captured = capsys.readouterr()
        assert "background:#181818" in captured.out
        assert "#e9e9e9" in captured.out
        assert "<style>" in captured.out

    finally:
        sys.argv = original_argv
        os.unlink(temp_file)


def test_light_theme_default(capsys):
    """Test light theme is applied by default."""
    markdown_content = "# Test\n\nContent."

    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write(markdown_content)
        temp_file = f.name

    try:
        original_argv = sys.argv
        sys.argv = ["md2html.py", temp_file]

        main()

        captured = capsys.readouterr()
        assert "background:#181818" not in captured.out

    finally:
        sys.argv = original_argv
        os.unlink(temp_file)
