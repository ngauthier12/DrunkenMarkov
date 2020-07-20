import sys

from Parser import *
from Writer import *


def learn():
    argc = len(sys.argv)
    if argc < 5:
        print("Expecting depth, source(s) and destination paths")
        return False

    depth = int(sys.argv[2])
    parser = Parser(depth)

    for i in range(3, argc - 1):
        parser.read(sys.argv[i])
    parser.save(sys.argv[argc - 1])

    return True


def write():
    writer = Writer()
    argc = len(sys.argv)

    if argc < 4:
        print("Expecting data file(s) and output paths")
        return False

    for i in range(2, argc - 1):
        writer.load(sys.argv[i])
    writer.write(sys.argv[argc - 1])

    return True


def print_help():
    print("""
DrunkenMarkov ~~~ Help
-------------------------
Two commands are available. The first one to build a data-set from source file(s). 
The second one writes verbose from data-set(s).

py DrunkenMarkov.py --learn {depth} {sourceFile1 sourceFile2 ...} {dataFile}
    where depth is the recurrence depth (2 or 3 suggested, but can be more)
    where one or more sourceFile(s) can be specified, assuming UTF8 format.
    where the dataFile is exported as json, with UTF8 encoding.
    
py DrunkenMarkov.py --write {dataFile1 dataFile2 ...} {outputFile} 
    where one or more dataFile(s) can be specified, each of them being the output of a --learn call.
    where outputFile is exported as text, with UTF8 encoding.
    
Project is hosted on github, over here:
https://github.com/ngauthier12/DrunkenMarkov

""")
    return True


if __name__ == "__main__":

    command = ""
    if len(sys.argv) > 1:
        command = sys.argv[1]

    success = False

    if command == "--learn":
        success = learn()
    elif command == "--write":
        success = write()
    elif command == "--help":
        success = print_help()
    elif command != "":
        print("Unrecognized command")

    if not success:
        print("see command --help for argument description")
