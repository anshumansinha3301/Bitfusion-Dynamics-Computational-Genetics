import numpy as np
import matplotlib.pyplot as plt

# Simulation of allele frequency change hota hai over generations using Wright-Fisher model
def simulate_wright_fisher(p_init, generations, population_size):
    p_values = np.zeros(generations)
    p_values[0] = p_init
    
    for gen in range(1, generations):
        p = p_values[gen-1]
        num_alleles_A = np.random.binomial(population_size, p)
        p_values[gen] = num_alleles_A / population_size
        
    return p_values

# Parameters
generations = 100
population_size = 1000
p_init = 0.5

# Simulate krna hai for different initial allele frequencies
p_values_0_5 = simulate_wright_fisher(p_init, generations, population_size)
p_values_0_3 = simulate_wright_fisher(0.3, generations, population_size)
p_values_0_7 = simulate_wright_fisher(0.7, generations, population_size)

# Plot results
plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
plt.plot(p_values_0_5, label='p0=0.5')
plt.xlabel('Generations')
plt.ylabel('Allele Frequency')
plt.title('Initial p = 0.5')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(p_values_0_3, label='p0=0.3', color='green')
plt.xlabel('Generations')
plt.ylabel('Allele Frequency')
plt.title('Initial p = 0.3')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(p_values_0_7, label='p0=0.7', color='red')
plt.xlabel('Generations')
plt.ylabel('Allele Frequency')
plt.title('Initial p = 0.7')
plt.legend()

plt.tight_layout()
plt.show()
