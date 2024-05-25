import heapq

def calculate_mex(piles):
    """ Calculate the minimum excludant (mex) of given piles. """
    smallest_nonnegative = 0
    while smallest_nonnegative in piles:
        smallest_nonnegative += 1
    return smallest_nonnegative

def main():
    # Input from the user for the number of piles and their respective sizes
    number_of_piles = int(input("Enter the number of piles: "))
    piles = []
    print("Enter the number of sticks in each pile:")
    for _ in range(number_of_piles):
        pile_size = int(input())
        piles.append(pile_size)
    
    # Using a heap to manage the piles (optional here as we need it only for mex calculation)
    heapq.heapify(piles)

    # Calculating the nimber by XORing all pile sizes
    nimber = 0
    for pile in piles:
        nimber ^= pile
    
    # Calculate the mex of the heap
    mex = calculate_mex(piles)
    
    print(f"The nimber (nim-sum) of the game is: {nimber}")
    print(f"The minimum excludant (mex) of the game is: {mex}")

if __name__ == "__main__":
    main()
