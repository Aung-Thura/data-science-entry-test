def check_divisibility(num, divisor):
    """
    Task 1:
    Checks if num is divisible by divisor using the modulo operator.
    """
    # Validate that both inputs are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Both inputs must be numeric."
    
    # Check divisibility (remainder is 0)
    return num % divisor == 0

# Task 2: Invocation Scenarios
scenario_1 = check_divisibility(6, 2)
scenario_2 = check_divisibility(7, 3)

print(scenario_1)  # Output: True
print(scenario_2)  # Output: False
