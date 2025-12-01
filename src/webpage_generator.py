from blocks_helper import *
from htmlnode import *
import os
from pathlib import Path

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for each in blocks:
        if each.startswith("# "):
            return each.lstrip('# ').strip()
            break
    raise Exception("there should be ay least 1 header block")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
        
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, root_content_dir):
    for item in dir_path_content.iterdir():
        if item.is_file():
            text = item.read_text()
            html_strings_of_item = markdown_to_html_node(text).to_html()

            rel = item.relative_to(root_content_dir)
            new_path = dest_dir_path / rel.with_suffix(".html")
            new_path.parent.mkdir(parents=True, exist_ok=True)

            f = open(template_path)   # open tempalte path markdown
            content_of_template_path = f.read()
            f.close()
            title = extract_title(text)
            content_of_template_path = content_of_template_path.replace("{{ Title }}", title)
            content_of_template_path = content_of_template_path.replace("{{ Content }}", html_strings_of_item)

            new_path.write_text(content_of_template_path)

        elif item.is_dir():
            generate_pages_recursive(item, template_path, dest_dir_path, root_content_dir)




    





    
   





