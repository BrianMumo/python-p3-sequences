#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        result = []  # Define the result to be printed and returned
    elif length == 1:
        result = [0]
    else:
        result = [0, 1]
        while len(result) < length:
            next_value = result[-1] + result[-2]
            result.append(next_value)
    
    print(result)  # Print the result to match tests expecting printed output
    return result  # Return the result to match tests expecting returned values
