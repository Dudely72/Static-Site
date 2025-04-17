import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType
from text2html import text_node_to_html_node





class TestText2HTML(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode("This is a text node", TextType.normal_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.bold_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")
    def test_italic_text(self):
        node = TextNode("This is an italic text node", TextType.italic_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")
    def test_code_text(self):
        node = TextNode("This is a code text node", TextType.code_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
    def test_link_text(self):
        node = TextNode("This is a link text node", TextType.link_text, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href":node.url})
    def test_image_text(self):
        node = TextNode("This is an image text node", TextType.image_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":node.url, "alt":node.text})

if __name__ == "__main__":
    unittest.main()