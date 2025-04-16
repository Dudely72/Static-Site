from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.normal_text:
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == TextType.bold_text:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.italic_text:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.code_text:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.link_text:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    if text_node.text_type == TextType.image_text:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    raise Exception("TextNode has invalid type")