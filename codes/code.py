import random

def simulate_coin_tosses(num_tosses, num_simulations):
    num_successes = 0
    for _ in range(num_simulations):
        tosses = [random.randint(0, 1) for _ in range(num_tosses)]  # 0 means tails, 1 means heads
        if any(toss == 1 for toss in tosses):
            num_successes += 1
    return num_successes / num_simulations

req_probability = 0.9
num_simulations = 100000  # Number of times to simulate the coin tosses

n = 1
while True:
    simulated_probability = simulate_coin_tosses(n, num_simulations)
    if simulated_probability > req_probability:
        break
    n += 1

print(f"Number of tosses needed to achieve a probability > {req_probability}: {n}")

