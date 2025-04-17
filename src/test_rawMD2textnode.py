import unittest
from textnode import TextNode, TextType
from rawMD2textnode import split_nodes_delimiter

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
    def only_delimiters(self):
        md_node = TextNode("____", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "_", TextType.italic_text)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "") #checks first content
        self.assertEqual(new_nodes[0].text_type, TextType.normal_text) #checks text type
        self.assertEqual(new_nodes[1].text, "")
        self.assertEqual(new_nodes[1].text_type, TextType.italic_text)
        self.assertEqual(new_nodes[2].text, "") 
        self.assertEqual(new_nodes[2].text_type, TextType.italic_text)
        self.assertEqual(new_nodes[3].text, "") #checks first content
        self.assertEqual(new_nodes[3].text_type, TextType.normal_text) #checks text type
    def only_code(self):
        md_node = TextNode("`code`", TextType.normal_text)
        new_nodes = split_nodes_delimiter([md_node], "`", TextType.code_text)
        self.assertEqual(len(new_nodes), 3)
        
        
    


if __name__ == "__main__":
    unittest.main()