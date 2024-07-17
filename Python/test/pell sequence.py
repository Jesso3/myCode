def generate_pell_sequence(limit):
    sequence = [0, 1]  # Initial values of Pell sequence
    a, b = sequence[0], sequence[1]

    while b <= limit:
        a, b = b, 2 * b + a
        sequence.append(b)

    return sequence

# Example usage
limit = 1000
pell_sequence = generate_pell_sequence(limit)
print(pell_sequence)
