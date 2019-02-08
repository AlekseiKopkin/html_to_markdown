# -*- coding: utf-8 -*-
"""
Tests for html_to_md module
"""

import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

import html_to_md


class Test(unittest.TestCase):
    def test_parse_empty_string(self):
        html_text = u''
        result = html_to_md.html_to_md(html_text)
        expected = u''
        self.assertEqual(result, expected)

    def test_ignored_tags(self):
        html_text = u'<html>Some text</html>'
        result = html_to_md.html_to_md(html_text)
        expected = u'Some text'
        self.assertEqual(result, expected)

    def test_tag_i(self):
        html_text = u'<i class="class1" id="1">Some text</i>'
        result = html_to_md.html_to_md(html_text)
        expected = u'*Some text*'
        self.assertEqual(result, expected)

    def test_tag_tt(self):
        html_text = u'<tt class="class1" id="1">Some text</tt>'
        result = html_to_md.html_to_md(html_text)
        expected = u'`Some text`'
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
