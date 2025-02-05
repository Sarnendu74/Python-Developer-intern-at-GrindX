# Create a function to merge two dictionaries and handle conflicts by summing the values of common keys.
def merge_dicts(dict1, dict2):
    # Create a new dictionary to store the merged result
    merged_dict = dict1.copy()  

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum values if key exists in both dictionaries
        else:
            merged_dict[key] = value  # Add new key-value pair

    return merged_dict

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged_result = merge_dicts(dict1, dict2)
print(merged_result) 
