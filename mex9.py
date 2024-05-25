import heapq

def interpret_rule(rule):
    """ Interprets the decimal rule to configure heap behavior. Returns a list of priorities based on rule digits. """
    # Remove the decimal point and convert each digit to an integer
    priorities = [int(char) for char in str(rule) if char != '.']
    return priorities

def main():
    print("Welcome to the Binary Heap Game")
    # Input the rule in decimal form
    decimal_rule = float(input("Enter the game rule as a decimal (e.g., 0.456): "))
    
    # Interpret the rule to get heap priorities
    heap_priorities = interpret_rule(decimal_rule)
    
    # Create a binary heap from these priorities
    heapq.heapify(heap_priorities)
    print(f"Initial heap based on rule {decimal_rule}: {heap_priorities}")
    
    # Example game operation: Pop the top element using heap rules
    if heap_priorities:
        top = heapq.heappop(heap_priorities)
        print(f"Top element popped from heap: {top}")
        print(f"Remaining heap: {heap_priorities}")
    else:
        print("Heap is empty after initial setup.")

if __name__ == "__main__":
    main()
