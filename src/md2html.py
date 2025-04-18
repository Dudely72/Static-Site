from htmlnode import HTMLNode, LeafNode, ParentNode
from MD2Blocks import *
from textnode import TextNode, TextType
from text2html import text_node_to_html_node
from rawMD2textnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.heading:
            level = block.find(" ")
            heading_level = block.count("#", 0, level)
            content = block[level:].strip()
            inline_nodes = text_to_children(content)
            child_nodes.append(ParentNode(tag=f"h{heading_level}", children=inline_nodes))
        
        elif block_type == BlockType.paragraph:
            content = block.replace("\n", " ").strip()
            inline_nodes = text_to_children(content)
            child_nodes.append(ParentNode(tag="p", children=inline_nodes))
       
        elif block_type == BlockType.code:
            lines = block.split("\n")
            code_text = "\n".join(lines[1:-1]) + "\n"
            code_node = LeafNode(tag=None, value=code_text)
            pre_node = ParentNode(tag="pre", children=[ParentNode(tag="code", children=[code_node])])
            child_nodes.append(pre_node)
        
        elif block_type == BlockType.quote:
            quote_lines = [line.lstrip("> ").strip() for line in block.split("\n")]
            quote_text = " ".join(quote_lines)
            inline_nodes = text_to_children(quote_text)
            child_nodes.append(ParentNode(tag="blockquote", children=inline_nodes))
        
        elif block_type == BlockType.unordered_list:
            li_nodes = [
                ParentNode(tag="li", children=text_to_children(line[2:].strip()))
                for line in block.split("\n")
            ]
            child_nodes.append(ParentNode(tag="ul", children=li_nodes))
        
        elif block_type == BlockType.ordered_list:
            li_nodes = [
                ParentNode(tag="li", children=text_to_children(line[line.find(".")+1:].strip()))
                for line in block.split("\n")
            ]
            child_nodes.append(ParentNode(tag="ol", children=li_nodes))
    
    return ParentNode(tag="div", children=child_nodes)
    
        
