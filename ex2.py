def calculate_mex(numbers):
    """
    Calculate the Minimum EXcluded value (MEX) from a set of non-negative integers.
    
    Parameters:
    numbers (set of int): A set of non-negative integers.
    
    Returns:
    int: The smallest non-negative integer not present in the set.
    """
    num = 0
    while num in numbers:
        num += 1
    return num

def main():
    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter a list of non-negative integers separated by spaces: ")
    
    # Convert the input string to a set of integers
    numbers = set(map(int, user_input.split()))
    
    # Calculate the MEX
    mex = calculate_mex(numbers)
    
    # Print the result
    print("MEX of the set is:", mex)

# Call the main function to run the program
if __name__ == "__main__":
    main()
