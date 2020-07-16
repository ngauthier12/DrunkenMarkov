import sys

if __name__ == "__main__":

    command = ""
    if len(sys.argv) > 1:
        command = sys.argv[1]

    if command == "--learn":
        print("learning")
    elif command == "--write":
        print("writing")
    elif command == "--help":
        print("help") #TODO
    else:
        if command != "":
            print("Unrecognized command")
        print("see command --help for argument description")