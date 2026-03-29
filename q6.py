def find_first_negative(lst):
    """
    Task 1:
    Uses a while loop to find and return the first negative number in a list.
    """
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    
    return "No negatives"

# Task 2: Invocation Scenarios
scenario_1 = find_first_negative([3, 5, -6, 7, -2, 8])
scenario_2 = find_first_negative([2, 10, 7, 0])

print(scenario_1)  # Output: -1
print(scenario_2)  # Output: No negatives
