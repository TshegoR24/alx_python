import sys

def print_arguments(argv):
    num_arguments = len(argv) - 1  # The first argument is the script name itself

    print(f"Number of argument(s): {num_arguments}", end='')
    if num_arguments == 0:
        print(" .")
    else:
        print(":")
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv)
