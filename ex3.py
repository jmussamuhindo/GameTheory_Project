def calculate_mex(numbers, initial=204):
    """
    Calculate the Minimum EXcluded value (MEX) from a set of non-negative integers,
    starting with a predefined initial value if no smaller MEX is found.
    
    Parameters:
    numbers (set of int): A set of non-negative integers.
    initial (int): Initial default value for MEX if no smaller MEX is found.
    
    Returns:
    int: The smallest non-negative integer not present in the set or the initial value.
    """
    # Start checking from 0 up to the initial value
    for num in range(initial):
        if num not in numbers:
            return num
    return initial

def main():
    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter a list of numbers (only the number 0 is valid in this context): ")
    
    # Convert the input string to a set of integers
    numbers = set(map(int, user_input.split()))
    
    # Filter to include only 0 if it is in the input, as per the specified range [0, 0]
    numbers = {num for num in numbers if num == 0}
    
    # Calculate the MEX
    mex = calculate_mex(numbers)
    
    # Print the result
    print("MEX of the set is:", mex)

# Call the main function to run the program
if __name__ == "__main__":
    main()
