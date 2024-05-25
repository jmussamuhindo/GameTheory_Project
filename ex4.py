INITIAL = 204

def mex(number_set):
    number = 0
    while number in number_set:
        number += 1
    return number

numbers = [0, 0]

for pos in range(2, INITIAL):
    # Constructing the set with XOR operation for each element within the range 1 to pos
    prev_numbers_set = set(numbers[pos - mov - 1] ^ numbers[pos - 2] for mov in range(1, pos))
    # Append the mex of the constructed set to the numbers list
    numbers.append(mex(prev_numbers_set))

print(numbers[-1])
