import random

def simulate_coin_tosses(num_tosses, num_simulations):
    return sum(any(random.randint(0, 1) == 1 for _ in range(num_tosses)) for _ in range(num_simulations)) / num_simulations

def find_tosses_needed(req_probability, num_simulations, n=1):
    simulated_probability = simulate_coin_tosses(n, num_simulations)
    return n if simulated_probability > req_probability else find_tosses_needed(req_probability, num_simulations, n + 1)

req_probability = 0.9
num_simulations = 100000  # Number of times to simulate the coin tosses

n = find_tosses_needed(req_probability, num_simulations)

print(f"Number of tosses needed to get atleast 1 Heads > {req_probability}: {n}")

