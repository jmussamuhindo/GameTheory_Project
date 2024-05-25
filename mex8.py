def main():
    print("Welcome to the Binary Game Theory Calculator")
    
    # User inputs the number of piles in binary form
    try:
        number_of_piles = int(input("Enter the number of piles (in binary, e.g., '101' for 5): "), 2)
        piles = []
        
        print("Enter the number of sticks in each pile using binary notation:")
        for i in range(number_of_piles):
            binary_pile_size = input(f"Enter pile {i+1} size in binary: ")
            # Convert the binary input to an integer and store it
            pile_size = int(binary_pile_size, 2)
            piles.append(pile_size)
        
        # Calculating the nim-sum by XORing all pile sizes
        nim_sum = 0
        for pile in piles:
            nim_sum ^= pile  # XOR operation for nim-sum

        # Convert the nim-sum back to binary to display
        binary_nim_sum = bin(nim_sum)[2:]  # [2:] to remove the '0b' prefix from the binary output
        print(f"The nim-sum of the game in binary is: {binary_nim_sum}")
    
    except ValueError as e:
        print(f"Invalid input, please make sure to enter only binary numbers. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
