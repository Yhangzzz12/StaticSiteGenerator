import unittest
import re
from textnode import *
from htmlnode import *
from blocks_helper import *

class TestSplitDelimiterMethod(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_markdown_to_blocks_single_block_and_whitespace(self):
        md = """

    
This is a single block with extra blank lines around it    


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single block with extra blank lines around it"])


    def test_paragraph_block(self):
        block = "Just a normal line of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_levels(self):
        block = "### A level 3 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> first line\n> second line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "- item one\n- item two"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_bad_ordered_list_numbers(self):
        block = "1. first\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_unordered_list_falls_back_to_paragraph(self):
        block = "- good\nx bad"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
