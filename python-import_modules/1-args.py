import sys
def main():
    print("Number of arguments: {}.".format(len(sys.argv)))
    if len(sys.argv) > 0:
        for i in range(1, len(sys.argv)):
            print("Argument {}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    main()