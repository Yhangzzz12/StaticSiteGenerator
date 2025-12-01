import os
import shutil
from webpage_generator import *
from pathlib import Path
''' copies all the contents from a source directory to a destination directory (in our case, static to public)'''
def copy_from_src_to_des(old_path, new_path):
    if os.path.isfile(old_path):
        os.mkdir(new_path)
        shutil.copy(old_path, new_path)
        return 
    else:
        os.mkdir(new_path)
        for each in os.listdir(old_path):
            from_path = os.path.join(old_path, each)
            dest_path = os.path.join(new_path, each)
            copy_from_src_to_des(from_path, dest_path)


def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    copy_from_src_to_des("./static", "./public")
    generate_pages_recursive(Path("./content"), "template.html", Path("./public"), Path("./content") )
    
    

main()
