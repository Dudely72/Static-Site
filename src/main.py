import os
import sys
from textnode import TextNode, TextType
from copier import *
from website import generate_page, generate_pages_recursively


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    logging.info(f"Basepath set to: {basepath}")
    
    copy_directory("static", "docs")
    logging.info("Copied static files to docs.")

    generate_pages_recursively("content", "template.html", "docs", basepath=basepath)
    logging.info("Finished generating pages.")

main()
