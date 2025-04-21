from md2html import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.lstrip('#').strip()
            return header
    raise ValueError("No h1 title found in markdown")

def generate_page(from_path, template_path, dest_path, basepath ="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)


    
    filled_template = template_content.replace("{{ Title }}", title)
    filled_template = filled_template.replace("{{ Content }}", html_content)

    if not basepath.endswith("/"):
        basepath += "/"

    filled_template = filled_template.replace('href="/', f'href="{basepath}')
    filled_template = filled_template.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(filled_template)
    

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for root, dir, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                markdown_path = os.path.join(root, file)

                relative_path = os.path.relpath(markdown_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                generate_page(from_path=markdown_path, template_path=template_path, dest_path=dest_path, basepath="/Static-Site/")
                
