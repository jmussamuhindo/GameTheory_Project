def main():
    print("Welcome to the Game Theory Calculator")
    # Example of user input for rules or configurations
    try:
        number_of_piles = int(input("Enter the number of piles: "))
        piles = []
        for i in range(number_of_piles):
            pile_size = int(input(f"Enter the number of sticks in pile {i+1}: "))
            piles.append(pile_size)
        
        # Suppose we're calculating something with these piles, such as the nim-sum
        nim_sum = 0
        for pile in piles:
            nim_sum ^= pile  # XOR operation for nim-sum

        print(f"The nim-sum of the game is: {nim_sum}")
    
    except ValueError as e:
        print(f"Invalid input, please enter numeric values only. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
