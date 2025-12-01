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

   
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, root_content_dir, basepath):
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
            content_of_template_path = content_of_template_path.replace('href="/' , f'href="{basepath}')
            content_of_template_path = content_of_template_path.replace('src="/' , f'src="{basepath}')

            new_path.write_text(content_of_template_path)

        elif item.is_dir():
            generate_pages_recursive(item, template_path, dest_dir_path, root_content_dir, basepath)




    





    
   





