def mex(number_set):
    number = 0
    while number in number_set:
        number += 1
    return number

def main():
    # Define the INITIAL constant
    INITIAL = 204

    # Get user input for the initial numbers
    try:
        numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by space.")
        return

    # Extend the numbers list until it has INITIAL elements
    while len(numbers) < INITIAL:
        prev_numbers_set = {numbers[len(numbers) - mov - 1] ^ numbers[len(numbers) - 2] for mov in range(1, len(numbers))}
        numbers.append(mex(prev_numbers_set))

    print("The final number in the sequence is:", numbers[-1])

if __name__ == "__main__":
    main()
