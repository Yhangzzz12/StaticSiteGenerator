import os
import shutil
from webpage_generator import *
from pathlib import Path
import sys
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
    basepath = sys.argv[1] if len(sys.argv)>1 else "/"

    if os.path.exists("./docs"):
        shutil.rmtree("./docs")

    copy_from_src_to_des("./static", "./docs")
    generate_pages_recursive(Path("./content"), "template.html", Path("./docs"), Path("./content"), basepath )
    
    

main()
