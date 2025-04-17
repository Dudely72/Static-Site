import unittest
from textnode import TextNode, TextType
from rawMD2textnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

class TestRawMD2TextNode(unittest.TestCase):
    def test_basic_function(self):
        md_node = TextNode("This is `code` here", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "`", TextType.code_text)
        self.assertEqual(len(new_nodes), 3)   #checks length of result list
        self.assertEqual(new_nodes[0].text, "This is ") #checks first content
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text) #checks text type
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.code_text)
        self.assertEqual(new_nodes[2].text, " here") 
        self.assertEqual(new_nodes[2].text_type, TextType.normal_text)
    def test_multiple_delimiter_pairs(self):
        md_node = TextNode("This is `code` and more `code` here", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "`", TextType.code_text) 
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is ") #checks first content
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text) #checks text type
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.code_text)
        self.assertEqual(new_nodes[2].text, " and more ") 
        self.assertEqual(new_nodes[2].text_type, TextType.normal_text)
        self.assertEqual(new_nodes[3].text, "code") #checks first content
        self.assertEqual(new_nodes[3].text_type, TextType.code_text) #checks text type
        self.assertEqual(new_nodes[4].text, " here")
        self.assertEqual(new_nodes[4].text_type, TextType.normal_text)
    def test_no_delimiter(self):
        md_node = TextNode("This is plain text", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "`", TextType.code_text)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text)
    def test_italics_delimiter(self):
        md_node = TextNode("This is _italics_ here", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "_", TextType.italic_text)
        self.assertEqual(len(new_nodes), 3)   #checks length of result list
        self.assertEqual(new_nodes[0].text, "This is ") #checks first content
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text) #checks text type
        self.assertEqual(new_nodes[1].text, "italics")
        self.assertEqual(new_nodes[1].text_type, TextType.italic_text)
        self.assertEqual(new_nodes[2].text, " here") 
        self.assertEqual(new_nodes[2].text_type, TextType.normal_text)
    def test_bold_delimiter(self):
        md_node = TextNode("This is **bold** here", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "**", TextType.bold_text)
        self.assertEqual(len(new_nodes), 3)   #checks length of result list
        self.assertEqual(new_nodes[0].text, "This is ") #checks first content
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text) #checks text type
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.bold_text)
        self.assertEqual(new_nodes[2].text, " here") 
        self.assertEqual(new_nodes[2].text_type, TextType.normal_text)
    def test_empty_string(self):
        md_node = TextNode("", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "`", TextType.code_text)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "")
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text)
    def test_only_delimiters(self):
        md_node = TextNode("____", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "_", TextType.italic_text)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0].text, "") #checks first content
        self.assertEqual(new_nodes[0].text_type, TextType.italic_text) #checks text type
        self.assertEqual(new_nodes[1].text, "")
        self.assertEqual(new_nodes[1].text_type, TextType.italic_text)
    def test_only_code(self):
        md_node = TextNode("`code`", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "`", TextType.code_text)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "code")


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.normal_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.normal_text),
                TextNode("image", TextType.image_text, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.normal_text),
                TextNode(
                    "second image", TextType.image_text, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.normal_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.normal_text),
                TextNode("link", TextType.link_text, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.normal_text),
                TextNode(
                    "second link", TextType.link_text, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes_all_features(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![image](https://example.com/img.jpg) and a [link](https://example.com)"
        nodes = text_to_textnodes(text)
        # Assert the number of nodes and check a few specific ones
        self.assertEqual(len(nodes), 10)
        assert nodes[0].text == "This is "
        assert nodes[1].text == "text"
        assert nodes[1].text_type == TextType.bold_text
        # ... more assertions
        
    def test_text_to_textnodes_nested(self):
        text = "This is **_bold and italic_**"
        nodes = text_to_textnodes(text)
        # Check the results

    def test_text_to_textnodes_plain(self):
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 1
        assert nodes[0].text == "Just plain text"
        assert nodes[0].text_type == TextType.normal_text
    


if __name__ == "__main__":
    unittest.main()