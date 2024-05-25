def calculate_mex(numbers):
    """
    Calculate the Minimum EXcluded value (MEX) from a set of non-negative integers.
    
    Parameters:
    numbers (set of int): A set of non-negative integers.
    
    Returns:
    int: The smallest non-negative integer not present in the set.
    """
    if not numbers:  # If the set is empty, MEX is 0
        return 0
    
    num = 0
    while num in numbers:
        num += 1
    return num

# Example usage
numbers = {0, 1, 2, 4, 5, 7}
mex = calculate_mex(numbers)
print("MEX of the set is:", mex)
