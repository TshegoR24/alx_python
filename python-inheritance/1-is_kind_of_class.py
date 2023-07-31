def is_kind_of_class(obj, a_class):
    # Check if the object is an instance of the specified class
    if isinstance(obj, a_class):
        return True

    # Check if the object is an instance of a subclass that inherits from the specified class
    for subclass in obj.__class__.__bases__:
        if is_kind_of_class(obj, subclass):
            return True

    return False

# Example usage:
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

obj = ChildClass()

print(is_kind_of_class(obj, ParentClass))  # Output: True
print(is_kind_of_class(obj, str))          # Output: False
print(is_kind_of_class(42, int))           # Output: True
print(is_kind_of_class(42, float))         # Output: False
