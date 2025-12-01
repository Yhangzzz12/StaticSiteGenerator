import unittest

from htmlnode import *
from textnode import TextNode, TextType
class TestText_to_Textnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_adjacent_images_with_text(self):
        md = (
            "Here is an image: ![sun](https://example.com/sun.jpg) wow another one right away ![moon](https://example.com/moon.png)"
        )
        nodes = text_to_textnodes(md)
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("sun", TextType.IMAGE, "https://example.com/sun.jpg"),
            TextNode(" wow another one right away ", TextType.TEXT),
            TextNode("moon", TextType.IMAGE, "https://example.com/moon.png"),
        ]
        self.assertEqual(nodes, expected)


    def test_long_text_mixed(self):
        s = (
            "Start " 
            "**bold** then some long plain text that goes on and on without stopping, "
            "with numbers 12345 and symbols !?;: and more words, "
            "_italic_ then more text, "
            "`code snippet` then even more, "
            "an image: ![alt text here](https://example.com/img.png) "
            "and a link: [BootDev](https://boot.dev) "
            "finally ending."
        )
        assert text_to_textnodes(s) == [
            TextNode("Start ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" then some long plain text that goes on and on without stopping, with numbers 12345 and symbols !?;: and more words, ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" then more text, ", TextType.TEXT),
            TextNode("code snippet", TextType.CODE),
            TextNode(" then even more, an image: ", TextType.TEXT),
            TextNode("alt text here", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" and a link: ", TextType.TEXT),
            TextNode("BootDev", TextType.LINK, "https://boot.dev"),
            TextNode(" finally ending.", TextType.TEXT),
        ]


    def test_multiple_images(self):
        s = (
            "Gallery: "
            "![one](https://ex.com/1.png), "
            "![two](https://ex.com/2.jpg) "
            "and finally ![three](https://ex.com/3.gif)."
        )
        assert text_to_textnodes(s) == [
            TextNode("Gallery: ", TextType.TEXT),
            TextNode("one", TextType.IMAGE, "https://ex.com/1.png"),
            TextNode(", ", TextType.TEXT),
            TextNode("two", TextType.IMAGE, "https://ex.com/2.jpg"),
            TextNode(" and finally ", TextType.TEXT),
            TextNode("three", TextType.IMAGE, "https://ex.com/3.gif"),
            TextNode(".", TextType.TEXT),
        ]