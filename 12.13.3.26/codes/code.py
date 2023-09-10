# Values of X and their corresponding probabilities
values = [2, 3, 4]
probabilities = [0.2, 0.5, 0.3]

# Calculate the mean (expected value) of X
mean = sum(x * p for x, p in zip(values, probabilities))

# Calculate the variance of X
variance = sum((x - mean)**2 * p for x, p in zip(values, probabilities))

# Calculate the standard deviation of X (square root of the variance)
std_deviation = variance**0.5  # Using exponentiation for square root

# Print the results
print(f"Mean (Expected Value): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

