def raise_exception_msg(message=""):
    class NameException(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return f"NameException: {self.message}"

    raise NameException(message)

# Example usage:
try:
    name = input("Enter your name: ")
    if not name.isalpha():
        raise_exception_msg("Name must contain only alphabets.")
    else:
        print("Hello, " + name)
except raise_exception_msg as ne:
    print(ne)
