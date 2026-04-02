from pathlib import Path as p
import os


# Path of folder that needs to be sorted
unsorted = p("./unsorted")



def main():
    sort()
    


def sort():
    files = [item for item in p.iterdir(unsorted) if not item.is_dir()]
    for file in files:
        _, extension = str(file).split(".")
        if p(extension).exists():
            pass
        else:
            os.mkdir(extension)
            # print(f"Folder {extension} created at {os.getcwd()}")
    
    #os.chdir(sorted)
    #for extension in extensions:
        #if p(extension).exists():
            #pass
        #else:
            #os.mkdir(extension)
            # print(f"Folder {extension} created at {os.getcwd()}")


if __name__ == "__main__":
    main()