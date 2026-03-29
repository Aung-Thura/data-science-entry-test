def swap(x, y):
    """
    Task 1:
    Swaps x and y using only x and y as variables via arithmetic.
    Returns -1 if inputs are not numeric.
    """
    # Validate numeric types
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swapping logic without a third variable
    x = x + y
    y = x - y
    x = x - y
    
    print(f"Swapped values: x = {x}, y = {y}")

# Task 2: Invocation Scenarios
scenario_1 = swap("Apple", 10)
scenario_2 = swap(9, 17)

if scenario_1 == -1:
    print(scenario_1)  # Output: -1

# scenario_2 Output: Swapped values: x = 17, y = 9
