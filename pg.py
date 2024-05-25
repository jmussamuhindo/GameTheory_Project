""" (9) Even-Nim and Odd-Nim are like Nim in that they are played with
piles of stones. However, in Even-Nim a move consists of removing
a positive even number of stones from a pile, while in Odd-Nim a
move removes an odd number. (Note that a single pile of 1 stone is
thus a terminal position in Even-Nim.)

(a) Find a sequence of integers \(a_0, a_1, \ldots\) so that a pile of size \(i\) in
Odd-Nim is equivalent to *\(a_i\).

(b) Find a sequence of integers \(b_0, b_1, \ldots\) so that a pile of size \(i\) in
Even-Nim is equivalent to *\(b_i\).
 """
 
import pandas as pd

def mex(s):
    """Calculate the Minimum EXcludant of a set of numbers."""
    m = 0
    while m in s:
        m += 1
    return m

def calculate_odd_nim(n):
    """Calculate the nimbers for Odd-Nim up to size n."""
    odd_nim = [0] * (n + 1)  # Initialize the nimber list with zeroes
    for i in range(1, n + 1):
        reachable = set()
        # Iterate over possible odd moves
        for move in range(1, i + 1, 2):
            if i - move >= 0:
                reachable.add(odd_nim[i - move])
        odd_nim[i] = mex(reachable)
    return odd_nim

def calculate_even_nim(n):
    """Calculate the nimbers for Even-Nim up to size n."""
    even_nim = [0] * (n + 1)  # Initialize the nimber list with zeroes
    for i in range(2, n + 1):  # Starts from 2 since 0 and 1 are special cases
        reachable = set()
        # Iterate over possible even moves
        for move in range(2, i + 1, 2):
            if i - move >= 0:
                reachable.add(even_nim[i - move])
        even_nim[i] = mex(reachable)
    # Single stone is a terminal position in Even-Nim
    even_nim[1] = 0
    return even_nim

def display_nim_sequences(n):
    odd_nim_sequence = calculate_odd_nim(n)
    even_nim_sequence = calculate_even_nim(n)
    
    # Create a DataFrame for better visualization
    df = pd.DataFrame({
        'Pile Size': range(n + 1),
        'Odd-Nim': odd_nim_sequence,
        'Even-Nim': even_nim_sequence
    })
    
    # Print the DataFrame
    print(df)

# Generate and display the sequences for n = 20
display_nim_sequences(20)
