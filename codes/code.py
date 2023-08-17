import math

desired_probability = 0.9
coin_probability = 0.5
# calculating the integer value n 
n = math.ceil(math.log(1 - desired_probability, 1 - coin_probability))

print(f"The man must toss the coin at least {n} times.")



