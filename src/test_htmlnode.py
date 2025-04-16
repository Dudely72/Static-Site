import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # HTMLNode Parent Class tests
    def test_eq(self):
        node = HTMLNode("a", "this is the html value", ["node3", "node4", "node5"], {"key":"value"})
        node2 = HTMLNode("a", "this is the html value", ["node3", "node4", "node5"], {"key":"value"})
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node3 = HTMLNode("a", "this is the html value", ["node8", "node9", "node10"], {"key":"value"})
        node4 = HTMLNode("a", "this is also the html value", ["node3", "node4", "node5"], {"key":"value"})
        self.assertNotEqual(node3, node4)
    def test_eq_no_input(self):
        node5 = HTMLNode()
        node6 = HTMLNode()
        self.assertEqual(node5, node6)
    def test_not_eq_value(self):
        node7 = HTMLNode("a", "this is the html value", ["node3", "node4", "node5"], {"key":"value"})
        node8 = HTMLNode("a", "this is the html value", ["node1", "node2", "node3"], {"key":"value"})
        self.assertNotEqual(node7, node8)
    def test_props_to_html_eq(self):
        node9 = HTMLNode("a", "this is the html value", ["node3", "node4", "node5"], {"key":"value"})
        node10 = HTMLNode("a", "this is the html value", ["node3", "node4", "node5"], {"key":"value"})
        trial1 = node9.props_to_html()
        trial2 = node10.props_to_html()
        self.assertEqual(trial1, trial2)
    def test_props_to_html_not_eq(self):
        node11 = HTMLNode("a", "this is the html value", ["node3", "node4", "node5"], {"key":"value"})
        node12 = HTMLNode("b", "this is also the html value", ["node6", "node7", "node8"], {"key1":"value1"})
        trial3 = node11.props_to_html
        trial4 = node12.props_to_html
        self.assertNotEqual(trial3, trial4)
    # LEAFNode subclass tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    # ParentNode subclass tests
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

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("a", "second child")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><a>second child</a></div>")

    def test_to_html_with_multiple_children_and_grandchildren(self):
        grandchild_node1 = LeafNode("span", "grandchild")
        grandchild_node2 = LeafNode("a", "second grandchild")
        child_node1 = ParentNode("p", [grandchild_node1])
        child_node2 = ParentNode("r", [grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><p><span>grandchild</span></p><r><a>second grandchild</a></r></div>")

    def test_to_html_one_child_multiple_grandchildren(self):
        grandchild_node1 = LeafNode("span", "grandchild")
        grandchild_node2 = LeafNode("a", "second grandchild")
        child_node1 = ParentNode("p", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node1])
        self.assertEqual(parent_node.to_html(), "<div><p><span>grandchild</span><a>second grandchild</a></p></div>")

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()