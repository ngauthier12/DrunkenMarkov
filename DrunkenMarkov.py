import sys

from Parser import *


def learn():
    parser = Parser()
    argc = len(sys.argv)

    if argc < 4:
        print("Expecting source(s) and destination paths")
        return False

    for i in range(2, argc - 1):
        parser.read(sys.argv[i])
    parser.save(sys.argv[argc - 1])

    return True


def write():
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
