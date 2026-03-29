def swap(x, y):
    def swap(x, y):
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "-1"
    
    # Swapping logic using addition and subtraction
    # No temporary variable is used
    x = x + y  # x now holds the sum of both
    y = x - y  # y becomes the original value of x
    x = x - y  # x becomes the original value of y
    
    print(f"Swapped values: x = {x}, y = {y}")
    

    return
swap(1, 5)


