def find_and_replace(lst, find_val, replace_val):
    """
    Task 1:
    Replaces all occurrences of find_val with replace_val in the given list.
    """
    if not isinstance(lst, list):
        return "Input must be a list."

    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
            
    return lst
    
    
    
scenario_1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
scenario_2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")

print(scenario_1)  # Output: [1, 5, 3, 4, 5, 5]
print(scenario_2)  # Output: ['orange', 'banana', 'orange']
