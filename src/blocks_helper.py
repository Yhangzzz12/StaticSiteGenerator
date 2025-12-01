from enum import Enum
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE  = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block_text):
    if block_text.startswith(('# ', '## ' , '### ' , '#### ' , '##### ' , '###### ')):
        return BlockType.HEADING

    if block_text.startswith('```') and block_text.endswith('```'):
        return BlockType.CODE

    if block_text.startswith('>'):
        return BlockType.QUOTE

    if block_text.startswith('- '):
        for each in block_text.split('\n'):
            if not each.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block_text.startswith('1. '):
        ah = block_text.split('\n')
        for i in range(2, len(ah)+1):
            if not ah[i-1].startswith(f'{i}. '):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    new_block = []
    for each in blocks:
        each = each.strip()
        if each == "":
            continue
        new_block.append(each)
    return new_block




def text_to_children(text):
    list_of_html = []
    text_nodes = text_to_textnodes(text)
    for each in text_nodes:
        html_node = text_node_to_html_node(each)
        list_of_html.append(html_node)
    return list_of_html


def block_type_to_html_node(block_type, text):
    if block_type == BlockType.PARAGRAPH:
        new_text = text.split('\n')
        clean_text = (' ').join(new_text)
        return ParentNode(tag = 'p', children = text_to_children(clean_text), props = None)
    elif block_type == BlockType.HEADING:
        return h1_to_h6_htmlnode(block_type, text)
    elif block_type == BlockType.CODE:
        new_text = text.split('\n')
        inner = new_text[1:-1]
        clean_text = ('\n').join(inner) + '\n'
        code = ParentNode(tag='code', children = [code_text_to_html(clean_text)], props = None)
        return ParentNode(tag = 'pre', children = [code], props = None)
    elif block_type == BlockType.QUOTE:
        bq = ''
        items = text.split('\n')
        for item in items:
            clean_item = item.lstrip('>').strip()
            bq += f'{clean_item}\n'
        return ParentNode(tag = 'blockquote', children = text_to_children(bq), props = None)
    elif block_type == BlockType.UNORDERED_LIST:
        li_nodes = []
        items = text.split('\n')
        for item in items:
            clean_item = item.lstrip('- ').strip()
            li_nodes.append(ParentNode(tag='li',children =text_to_children(clean_item), props= None))
        return ParentNode(tag="ul", children=li_nodes, props=None)
    elif block_type == BlockType.ORDERED_LIST:
        li_nodes = []
        clean_items =[]
        items = text.split('\n')
        for i in range(1, len(items)+1):
            clean_item = items[i-1].lstrip(f'{i}. ').strip()
            clean_items.append(clean_item)
        
        for clean_item in clean_items:
            li_nodes.append(ParentNode(tag='li',children = text_to_children(clean_item), props= None))
        return ParentNode(tag="ol", children=li_nodes, props=None)


def code_text_to_html(text):
    code_text_node = TextNode(text, TextType.TEXT)
    return text_node_to_html_node(code_text_node)


def h1_to_h6_htmlnode(block_type, text):
    if block_type != BlockType.HEADING:
        raise Exception('It should be a heading block')
    if text.startswith('# '):
        clean_text = text.lstrip('# ').strip()
        return ParentNode(tag = 'h1' , children = text_to_children(clean_text), props = None)
    if text.startswith('## '):
        clean_text = text.lstrip('## ').strip()
        return ParentNode(tag = 'h2' ,children = text_to_children(clean_text), props = None)
    if text.startswith('### '):
        clean_text = text.lstrip('### ').strip()
        return ParentNode(tag = 'h3', children = text_to_children(clean_text), props = None)
    if text.startswith('#### '):
        clean_text = text.lstrip('#### ').strip()
        return ParentNode(tag = 'h4' ,children = text_to_children(clean_text), props = None)
    if text.startswith('##### '):
        clean_text = text.lstrip('##### ').strip()
        return ParentNode(tag = 'h5', children = text_to_children(clean_text), props = None)
    if text.startswith('###### '):
        clean_text = text.lstrip('###### ').strip()
        return ParentNode(tag = 'h6', children = text_to_children(clean_text), props = None)
    
'''
Above are all my helpers
Below is my final recipe'''

def markdown_to_html_node(markdown):
    list_of_parent = []
    blocks = markdown_to_blocks(markdown)
    for each in blocks:
# print(repr(each))
        block_type = block_to_block_type(each)
        parent_block_node = block_type_to_html_node(block_type, each)
        list_of_parent.append(parent_block_node)
    div_parent_node = ParentNode(tag='div', children = list_of_parent, props = None )
# print(div_parent_node.to_html())
    return div_parent_node  

'''
md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
markdown_to_html_node(md)
'''



md2 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

# markdown_to_html_node(md2)
        
