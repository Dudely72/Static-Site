import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.bold_text)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node3 = TextNode("This is a text node", TextType.bold_text)
        node4 = TextNode("This is also a text node", TextType.italic_text)
        self.assertNotEqual(node3, node4)
    def test_eq_urls(self):
        node5 = TextNode("This is a text node", TextType.bold_text, "www.booger.com")
        node6 = TextNode("This is a text node", TextType.bold_text, "www.booger.com")
        self.assertEqual(node5, node6)
    def test_not_eq_urls(self):
        node7 = TextNode("This is a text node", TextType.bold_text)
        node8 = TextNode("This is a text node", TextType.bold_text, "www.fart.com")
        self.assertNotEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()