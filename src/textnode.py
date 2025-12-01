from enum import Enum
import re
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'



def extract_markdown_images(text):
    list_of_tuple = []
    matches = re.findall(r"\[([\w\s\W]*?)\]\(([\w\W\d]*?)\)", text)
    for each in matches:
        list_of_tuple.append(each)
    return list_of_tuple

def extract_markdown_links(text):
    list_of_tuple = []
    matches = re.findall(r"\[([\w\s\W]*?)\]\(([\w\W\d]*?)\)", text)
    for each in matches:
        list_of_tuple.append(each)
    return list_of_tuple





  


