def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as ne:
        print(f"NameError: {ne}")

# Test the function
try:
    raise_exception_msg("Custom message for the exception")
except NameError as ne:
    print(f"Caught the exception: {ne}")
