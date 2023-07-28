import sys

def main():
    argv_len = len(sys.argv)
    
    print(f"Number of argument(s): {argv_len - 1}", end="")
    
    if argv_len == 1:
        print(".")
    else:
        print(f", followed by\n:")
        for i in range(1, argv_len):
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    main()

