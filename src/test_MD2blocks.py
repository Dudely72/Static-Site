import unittest
from MD2Blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMD2Blocks(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        md = """# This is a heading

This is a paragraph with **bold** text.

- Item 1
- Item 2
- Item 3"""
        expected = [
            "# This is a heading",
            "This is a paragraph with **bold** text.",
            "- Item 1\n- Item 2\n- Item 3"
        ]
        self.assertEqual (markdown_to_blocks(md), expected)

    def test_extra_whitespace(self):
        markdown = """  # Heading    

    

    Paragraph text.     

- List Item 1
- List Item 2

"""
        expected = [
            "# Heading",
            "Paragraph text.",
            "- List Item 1\n- List Item 2"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_only_whitespace(self):
        self.assertEqual(markdown_to_blocks("   \n\n   "), [])

    def test_single_paragraph(self):
        markdown = "Just one paragraph with no double newlines."
        expected = ["Just one paragraph with no double newlines."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_newlines(self):
        markdown = "Paragraph 1\n\n\n\nParagraph 2\n\n\n\n\n\nParagraph 3"
        expected = ["Paragraph 1", "Paragraph 2", "Paragraph 3"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_block_to_block_type(self):
        assert block_to_block_type("# Heading") == BlockType.heading
        assert block_to_block_type("```print('Hello')```") == BlockType.code
        assert block_to_block_type("> Quote line\n> Another line") == BlockType.quote
        assert block_to_block_type("- Item 1\n- Item 2") == BlockType.unordered_list
        assert block_to_block_type("1. First\n2. Second\n3. Third") == BlockType.ordered_list
        assert block_to_block_type("This is a paragraph of text.") == BlockType.paragraph




if __name__ == "__main__":
    unittest.main()