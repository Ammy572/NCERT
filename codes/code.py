import math
import numpy as np
from scipy.stats import bernoulli

def calculate_num_tosses(target_probability):
    # Using the formula to calculate the number of tosses needed
    num_tosses = math.ceil(math.log(1 - target_probability, 0.5))
    return num_tosses
    
target_probability = 0.9  # 90% probability of at least one head
num_tosses_needed = calculate_num_tosses(target_probability)

print(f"Number of coin tosses needed to exceed {target_probability*100}% probability: {num_tosses_needed}")
data_bern = bernoulli.rvs(size=100000 ,p=target_probability)
err_ind = np.nonzero(data_bern == 1)
#print(np.size(err_ind))
print("Probability-simulation,actual:",np.size(err_ind)/100000)
#print("Samples generated:",data_bern)
