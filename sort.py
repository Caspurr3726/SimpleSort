from pathlib import Path as p
import os
import shutil

# Path of folder that needs to be sorted.
unsorted = p("./unsorted")


def main():
    sort()
    

def sort():
    # Creates a list, named files, containing every item that isn't a directory in the unsorted folder.
    files = [item for item in p.iterdir(unsorted) if not item.is_dir()]
    # Runs through each file in files, checking their extension, and making a folder for that extension if one doesn't already exist.
    for file in files:
        _, extension = str(file).split(".")
        if p(extension).exists():
            pass
        else:
            os.mkdir(extension)
            # Debug : print(f"Folder {extension} created at {os.getcwd()}")
        
        shutil.move(file, p(extension))
    

if __name__ == "__main__":
    main()