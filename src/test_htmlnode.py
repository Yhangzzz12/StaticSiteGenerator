import unittest

from textnode import *
from htmlnode import *  # if you need it directly

class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNODE(tag = "a", value= "Hello, FYP", props = {'href': "https://www.google.com"} )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"' )

    def test_value(self):
        node = HTMLNODE(
            tag =  "p" , 
            value = "This is a paragraph." ,  
            children = None, 
            props = None
        )
        self.assertEqual(node.value, "This is a paragraph." )

    def test_repr(self):
        node = HTMLNODE(
            tag =  "p" , 
            value = "This is a paragraph." ,  
            children = None, 
            props = None
        )
        self.assertEqual(node.__repr__(),
         "HTMLNODE(p, This is a paragraph., None, None)")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_image_node_to_html(self):
        node = TextNode("A bear", TextType.IMAGE, "https://example.com/bear.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "https://example.com/bear.png",
            "alt": "A bear",
        })

if __name__ == "__main__":
    unittest.main()



