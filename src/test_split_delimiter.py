import unittest

from htmlnode import *

class TestSplitDelimiterMethod(unittest.TestCase):
    def test_delimiter_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])

    def test_delimiter_2(self):
        node = TextNode("`code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("code block", TextType.CODE),
            ])

    def test_delimiter_3(self):
        node = TextNode("This is text with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a code block word", TextType.TEXT),
            ])
    
    def test_delimiter_4(self):
        node = TextNode("https://www.boot.dev", TextType.LINK)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node,node2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("https://www.boot.dev", TextType.LINK),
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])

    




if __name__ == "__main__":
    unittest.main()      
