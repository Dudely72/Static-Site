from textnode import TextNode, TextType

def main():
    node1 = TextNode("This is anchor text", TextType.link_text, "https.//www.bootdev.dev")
    print(node1)

main()
