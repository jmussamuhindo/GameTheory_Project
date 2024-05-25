import heapq

def interpret_rule(rule):
    """ Interprets the decimal rule to configure heap behavior. Returns a list of priorities based on rule digits. """
    # Remove the decimal point and convert each digit to an integer
    priorities = [int(char) for char in str(rule) if char != '.']
    return priorities

def calculate_mex(heap):
    """ Calculates the minimum excludant (mex) for a given heap, starting indexing from 1, ignoring 0. """
    seen = set(heap)  # Directly convert heap to set to avoid multiple pops
    mex = 1  # Start checking from 1, as 0 is not considered
    while mex in seen:
        mex += 1
    return mex

def calculate_nim_sum(heap):
    """ Calculates the nim-sum (XOR of all elements) for the game. """
    nim_sum = 0
    for element in heap:
        nim_sum ^= element
    return nim_sum

def main():
    print("Welcome to the Binary Heap Game")
    decimal_rule = float(input("Enter the game rule as a decimal (e.g., 0.456): "))
    heap_priorities = interpret_rule(decimal_rule)
    
    # Create a binary heap from these priorities
    heapq.heapify(heap_priorities)
    print(f"Initial heap based on rule {decimal_rule}: {heap_priorities}")

    # Calculate the mex and nim-sum of the heap
    mex = calculate_mex(heap_priorities)
    nim_sum = calculate_nim_sum(heap_priorities)
    print(f"The minimum excludant (mex) of the heap is: {mex}")
    print(f"The nim-sum of the game is: {bin(nim_sum)[2:]} (binary format)")

    # Optionally, find the maximum element in the heap
    if heap_priorities:
        max_element = max(heap_priorities)
        print(f"The maximum element in the heap is: {max_element}")
    else:
        print("Heap is empty.")

if __name__ == "__main__":
    main()
