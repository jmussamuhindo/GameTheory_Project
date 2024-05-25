import pandas as pd

def mex(s):
    """Calculate the Minimum EXcludant of a set of numbers."""
    m = 0
    while m in s:
        m += 1
    return m

def calculate_nimbers(n, move_set):
    """Calculate the nimbers for a game with given move set up to size n."""
    nimbers = [0] * (n + 1)  # Initialize the nimber list with zeroes
    for i in range(1, n + 1):
        reachable = set()
        # Iterate over possible moves
        for move in move_set:
            if i - move >= 0:
                reachable.add(nimbers[i - move])
        nimbers[i] = mex(reachable)
    return nimbers

def display_nimbers(n, game_types):
    nim_sequences = {}
    for game_name, move_set in game_types.items():
        nim_sequences[game_name] = calculate_nimbers(n, move_set)
    
    # Create a DataFrame for better visualization
    df = pd.DataFrame(nim_sequences)
    df.insert(0, 'Pile Size', range(n + 1))
    
    # Print the DataFrame
    print(df)

# Define move sets for different game types
game_types = {
    'Normal Nim': list(range(1, 21)),  # Any number from 1 to 20
    'Odd-Nim': list(range(1, 21, 2)),  # Odd numbers from 1 to 19
    'Even-Nim': list(range(2, 21, 2)), # Even numbers from 2 to 20
    'Custom-Nim': [1, 3, 4, 5]         # Custom moves
}

# Generate and display the sequences for n = 20
display_nimbers(20, game_types)
