def inherits_from(obj, a_class):
    # Get the class of the object
    obj_class = type(obj)

    # Traverse the inheritance chain until we reach the base object class (object)
    while obj_class != object:
        # Check if the current class is the specified class or inherits from it
        if obj_class is a_class:
            return True
        # Move up the inheritance chain
        obj_class = obj_class.__base__

    # If we reached the base object class without finding the specified class, return False
    return False
