from textnode import *
class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ''
        string_html = ''
        for key, value in self.props.items():
            string_html += f' {key}="{value}"'
        return string_html
    
    def __repr__(self):
        return f'HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value==None:
            raise ValueError
        if not self.tag:
            return self.value
        else:
            str_html = self.props_to_html()
            return  f"<{self.tag}{str_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props= None):
        super().__init__(tag=tag, children=children, props = props)
    
    def to_html(self):
        result = f'<{self.tag}>'
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError("No children")
        else:
            for each in self.children:
                result += each.to_html()
            result += f'</{self.tag}>'
        return result




def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag= None, value = text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value =text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value =text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value =text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value = text_node.text, props = {"href" : text_node.url })
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value = '', props = {"src" : text_node.url , "alt": text_node.text})





def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_list = []
    for each in old_nodes:
        if each.text_type != TextType.TEXT:
            text_list.append(each)
            continue
        splited_list = each.text.split(delimiter)
        if len(splited_list) %2 == 0:
            raise Exception("that's invalid Markdown syntax")
        for i in range(len(splited_list)):
            if i%2 ==0:
                if splited_list[i]:
                     text_list.append(TextNode(splited_list[i],TextType.TEXT))
            else:
                text_list.append(TextNode(splited_list[i],text_type))
    return text_list



def split_nodes_image(old_nodes):
    n = 1
    split_node = []
    for each_node in old_nodes:
        if each_node.text_type != TextType.TEXT:
            split_node.append(each_node)
            continue
        split_text = re.split(r"(!\[.*?\]\(.*?\))", each_node.text)
        markdown_images = extract_markdown_images(each_node.text)
        for i in range(len(split_text)):
            if not split_text[i]:
                continue
            if i % 2 ==0:
                split_node.append(TextNode(split_text[i],TextType.TEXT))
            else:
                split_node.append(TextNode(markdown_images[i-n][0],TextType.IMAGE,markdown_images[i-n][1]))
                n+=1
    return split_node


def split_nodes_link(old_nodes):
    n = 1
    split_node = []
    for each_node in old_nodes:
        if each_node.text_type != TextType.TEXT:
            split_node.append(each_node)
            continue
        split_text = re.split(r"(\[.*?\]\(.*?\))", each_node.text)
        markdown_images = extract_markdown_links(each_node.text)
        for i in range(len(split_text)):
            if not split_text[i]:
                continue
            if i % 2 ==0:
                split_node.append(TextNode(split_text[i],TextType.TEXT))
            else:
                split_node.append(TextNode(markdown_images[i-n][0],TextType.LINK,markdown_images[i-n][1]))
                n+=1
    return split_node



def text_to_textnodes(text):
    text_node = split_nodes_delimiter([TextNode(text,TextType.TEXT)], "**", TextType.BOLD)
    text_node = split_nodes_delimiter(text_node, "_", TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node, "`", TextType.CODE)
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)
    return text_node


    
                
    


        



        
    




        

        

        



    

        

