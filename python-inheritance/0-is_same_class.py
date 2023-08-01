def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class
