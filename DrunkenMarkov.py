import sys

from Parser import *
from Writer import *

depth = 2


def learn():
    parser = Parser(depth)
    argc = len(sys.argv)

    if argc < 4:
        print("Expecting source(s) and destination paths")
        return False

    for i in range(2, argc - 1):
        parser.read(sys.argv[i])
    parser.save(sys.argv[argc - 1])

    return True


def write():
    writer = Writer(depth)
    argc = len(sys.argv)

    if argc < 4:
        print("Expecting data file(s) and output paths")
        return False

    for i in range(2, argc - 1):
        writer.load(sys.argv[i])
    writer.write(sys.argv[argc - 1])

    return True


def print_help():
    # TODO -- write help
    print("help...")
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
