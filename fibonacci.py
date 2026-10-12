def generate_fibonacci(n: int) -> list[int]:
    # Handle edge case where no terms or invalid terms are requested
    if n <= 0:
        return []
    # Handle case for only one term
    if n == 1:
        return [0]
    
    # Initialize the sequence with the first two terms
    sequence = [0, 1]
    
    # Loop from the 3rd term up to n
    for i in range(2, n):
        # Add the sum of the last two elements to the list
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

# Example usage: Generate the first 10 Fibonacci numbers
num_terms = 10
print(f"First {num_terms} terms:", generate_fibonacci(num_terms))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
