import heapq

def interpret_rule(rule):
    """ Interprets the decimal rule to configure heap behavior. Returns a list of priorities based on rule digits. """
    # Remove the decimal point and convert each digit to an integer
    priorities = [int(char) for char in str(rule) if char != '.']
    return priorities

def calculate_mex(heap):
    """ Calculates the minimum excludant (mex) for a given heap. """
    # Since the heap can be modified, work on a copy
    temp_heap = list(heap)  # Create a shallow copy to avoid modifying the original heap
    seen = set()
    while temp_heap:
        element = heapq.heappop(temp_heap)
        seen.add(element)
    # Calculate mex
    mex = 0
    while mex in seen:
        mex += 1
    return mex

def main():
    print("Welcome to the Binary Heap Game")
    # Input the rule in decimal form
    decimal_rule = float(input("Enter the game rule as a decimal (e.g., 0.456): "))
    
    # Interpret the rule to get heap priorities
    heap_priorities = interpret_rule(decimal_rule)
    
    # Create a binary heap from these priorities
    heapq.heapify(heap_priorities)
    print(f"Initial heap based on rule {decimal_rule}: {heap_priorities}")
    
    # Calculate the mex of the heap
    mex = calculate_mex(heap_priorities)
    print(f"The minimum excludant (mex) of the heap is: {mex}")
    
    # Find the maximum element in the heap (inefficient way, suitable for small heaps)
    if heap_priorities:
        max_element = max(heap_priorities)
        print(f"The maximum element in the heap is: {max_element}")
    else:
        print("Heap is empty.")

if __name__ == "__main__":
    main()
