import unittest
from md2html import markdown_to_html_node

class TestMD2Blocks(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
text in a p
tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
This is text that _should_ remain
the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_headings(self):
        md = """# Heading 1
## Heading 2
### Heading 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>"
    )

    def test_inline_formatting(self):
        md = "Text with **bold**, _italic_, and `code`."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Text with <b>bold</b>, <i>italic</i>, and <code>code</code>.</p></div>"
        )


    def test_blockquote(self):
        md = "> This is a quote\n> across two lines."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote across two lines.</blockquote></div>"
    )

    def test_image(self):
        md = "Here is an image: ![alt text](https://example.com/image.png)"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Here is an image: <img src="https://example.com/image.png" alt="alt text"></p></div>'
        )


    def test_link(self):
        md = "Click [here](https://example.com) for more info."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Click <a href="https://example.com">here</a> for more info.</p></div>'
        )

    def test_unordered_list(self):
        md = "- Item one\n- Item two\n- Item three"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>"
        )

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>"
        )


if __name__ == "__main__":
    unittest.main()