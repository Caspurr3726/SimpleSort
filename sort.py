from pathlib import Path as p
import os
import shutil
import argparse
import sys


parser = argparse.ArgumentParser(usage="Sorts files into folders based on file extensions", description="A simple file sorter by Caspurr3726")
parser.add_argument("-cd", metavar= "Change Directory", default = "./unsorted", help = "change directory to pull files from", type = str)
parser.add_argument("-e", metavar= "Exclude", default = [], help = "file extensions excluded from sorting", type = list)
args = parser.parse_args()


def main():
    # If no input file is given, create the default "unsorted" folder
    if args.cd == ("./unsorted") and not p(args.cd).exists():
        os.mkdir("unsorted")
    sort()
    

def sort():
    input_folder = p(args.cd)
    exceptions = args.e


    # Creates a list, named files, containing every item that isn't a directory in the unsorted folder.
    files = [item for item in p.iterdir(input_folder) if not item.is_dir()]
    # Runs through each file in files, checking their extension, and making a folder for that extension if one doesn't already exist.
    for file in files:
        _, extension = str(file).split(".")
        if extension in exceptions:
            continue
        if p(extension).exists():
            pass
        else:
            os.mkdir(extension)
            # Debug : print(f"Folder {extension} created at {os.getcwd()}")
        
        
        shutil.move(file, p(extension))




if __name__ == "__main__":
    main()