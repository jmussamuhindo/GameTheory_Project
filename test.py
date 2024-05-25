def calculate_mex(s):
    """Calculate the MEX (minimum excludant) of a set of non-negative integers."""
    mex = 0
    while mex in s:
        mex += 1
    return mex

def generate_nim_positions(max_position):
    """Generate Nim positions and their corresponding MEX values up to a certain position."""
    positions = [set() for _ in range(max_position + 1)]  # Each position has a set of reachable Mex values
    mex_values = []
    
    for i in range(max_position + 1):
        # Calculate reachable positions and their MEX
        # Create a single set that contains all mex values reachable from current position
        reachable_positions = set()
        for j in range(1, i + 1):
            if i ^ j <= i:
                reachable_positions |= positions[i ^ j]  # Union of sets
        
        mex = calculate_mex(reachable_positions)
        positions[i].add(mex)
        mex_values.append(mex)
    
    return mex_values

# Example usage
max_position = 20  # This is the maximum position in Nim we are considering
nim_positions = generate_nim_positions(max_position)
print("Nim positions and their MEX values:")
for pos, mex in enumerate(nim_positions):
    print(f"Position {pos}: MEX = {mex}")
