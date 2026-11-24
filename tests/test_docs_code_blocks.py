"""Regression tests for code examples shown on the course's GitHub Pages site.

Run from repository root:
    python -m unittest discover -s tests -p "test_docs_code_blocks.py" -v

These tests protect the multiline examples that must use real newlines, not
literal backslash-n separators (the original Lesson 1 rendering defect).
"""

from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MULTILINE_EXAMPLE_IDS = {
    "01-introduction": (
        "c-hello", "c-vars", "c-input", "c-temp",
    ),
    "02-types-conditions": (
        "l2compare", "l2logic", "l2if", "l2nested",
        "l2task0", "l2task1", "l2task2", "l2task3", "l2task4", "l2match",
    ),
    "03-loops-strings": (
        "l3-for", "l3-while", "l3-sentinel", "l3-control", "l3-chars",
        "l3-slices", "l3-methods", "l3-solution-1", "l3-solution-2",
        "l3-solution-3", "l3-solution-4", "l3-solution-5",
        "l3-error-input", "l3-error-quit", "l3-error-division",
    ),
    "04-collections": (
        "l4-review", "l4-list", "l4-iteration", "l4-mutate",
        "l4-split", "l4-dict", "l4-freq", "l4-tuples", "l4-sets",
        "l4-sol-1", "l4-sol-2", "l4-sol-3", "l4-sol-4", "l4-sol-5",
    ),
    "05-functions-modules": (
        "l5-review", "l5-def", "l5-add", "l5-return", "l5-count",
        "l5-scope", "l5-math", "l5-module-word-tools", "l5-module-main",
        "l5-tests", "l5-sol1", "l5-sol2", "l5-sol3",
        "l5-sol4a", "l5-sol4b", "l5-sol5",
        "l5-computation", "l5-annotations", "l5-tuple-return",
        "l5-mutable", "l5-stdlib",
    ),
}


class LessonCodeParser(HTMLParser):
    """Collect code text and copy-button targets from one lesson page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._in_pre = False
        self._code_id = None
        self._parts = []
        self.code_blocks = []
        self.copy_targets = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "pre":
            self._in_pre = True
        elif tag == "code" and self._in_pre:
            self._code_id = attributes.get("id")
            self._parts = []
        elif tag == "button" and "data-copy" in attributes:
            self.copy_targets.append(attributes["data-copy"])

    def handle_data(self, data):
        if self._code_id is not None:
            self._parts.append(data)

    def handle_endtag(self, tag):
        if tag == "code" and self._code_id is not None:
            self.code_blocks.append((self._code_id, "".join(self._parts)))
            self._code_id = None
            self._parts = []
        elif tag == "pre":
            self._in_pre = False


class LessonCodeBlockTests(unittest.TestCase):
    def parse_lesson(self, lesson):
        page = ROOT / "docs" / "lessons" / lesson / "index.html"
        parser = LessonCodeParser()
        parser.feed(page.read_text(encoding="utf-8"))
        return parser

    def test_multiline_examples_have_real_line_breaks(self):
        for lesson, code_ids in MULTILINE_EXAMPLE_IDS.items():
            parser = self.parse_lesson(lesson)
            blocks = dict(parser.code_blocks)
            for code_id in code_ids:
                with self.subTest(lesson=lesson, code_id=code_id):
                    self.assertIn(code_id, blocks)
                    self.assertIn(
                        "\n",
                        blocks[code_id],
                        "Multiline example contains no real newline; check for escaped \\n.",
                    )

    def test_copy_buttons_match_code_blocks(self):
        for lesson in MULTILINE_EXAMPLE_IDS:
            parser = self.parse_lesson(lesson)
            code_ids = [code_id for code_id, _ in parser.code_blocks]
            with self.subTest(lesson=lesson):
                self.assertTrue(code_ids, "Expected Python code examples")
                self.assertEqual(len(code_ids), len(set(code_ids)))
                self.assertCountEqual(code_ids, parser.copy_targets)


if __name__ == "__main__":
    unittest.main()
