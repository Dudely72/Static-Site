import os
from textnode import TextNode, TextType
from copier import *
from website import generate_page, generate_pages_recursively


def main():
    copy_directory("./static", "./public")
    generate_pages_recursively("content", "template.html", "public")

main()
