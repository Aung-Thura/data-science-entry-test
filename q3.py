def update_dictionary(dct, key, value):
    """
    Task 1:
    Updates a dictionary with a new key-value pair.
    Prints the original value if the key exists before updating.
    """
    if key in dct:
        print(f"Original value: {dct[key]}")
    
    dct[key] = value
    return dct

# Task 2: Invocation Scenarios
scenario_1 = update_dictionary({}, "name", "Alice")
scenario_2 = update_dictionary({"age": 25}, "age", 26)

print(scenario_1) # Output: {'name': 'Alice'}
print(scenario_2) # Output: {'age': 26} (after printing 25)
