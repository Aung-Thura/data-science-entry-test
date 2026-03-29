def string_reverse(s):
    """
    Task 1:
    Reverses the given string s using slicing.
    """
    if not isinstance(s, str):
        return "Input must be a string."
    
    return s[::-1]

# Task 2: Invocation Scenarios
scenario_1 = string_reverse(1)
scenario_2 = string_reverse("Python")

print(scenario_1)  # Output: dlroW olleH
print(scenario_2)  # Output: nohtyP
