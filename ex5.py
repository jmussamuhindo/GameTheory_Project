def mex(number_set):
    number = 0
    while number in number_set:
        number += 1
    return number

def main():
    # Get user input for the initial two numbers
    try:
        first_num, second_num = map(int, input("Enter the first two numbers (separated by space): ").split())
        numbers = [first_num, second_num]
    except ValueError:
        print("Invalid input. Please enter two integers separated by space.")
        return

    # Get user input for the INITIAL value
    try:
        INITIAL = int(input("Enter the INITIAL value (a single integer): "))
    except ValueError:
        print("Invalid input. Please enter a single integer for the INITIAL value.")
        return

    # Use a while loop to calculate MEX until we reach the INITIAL count
    pos = 2
    while pos < INITIAL:
        # Constructing the set with XOR operation for each element within the range 1 to pos
        prev_numbers_set = {numbers[pos - mov - 1] ^ numbers[pos - 2] for mov in range(1, pos)}
        # Append the mex of the constructed set to the numbers list
        numbers.append(mex(prev_numbers_set))
        pos += 1

    print("The final number in the sequence is:", numbers[-1])

if __name__ == "__main__":
    main()
