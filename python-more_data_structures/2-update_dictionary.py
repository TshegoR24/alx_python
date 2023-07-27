def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dict, 'b', 10)  # Replaces the value of 'b' with 10
update_dictionary(my_dict, 'd', 4)   # Adds a new key-value pair 'd': 4
print(my_dict)
