import sys
def main():
    with open("variable_load_2.py", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("a = "):
            a = line.split("=")[1].strip()
            print(a)
if __name__ == "__main__":
    main()