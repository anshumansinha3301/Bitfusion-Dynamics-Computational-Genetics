import numpy as np
import matplotlib.pyplot as plt

# Simulation of genetic drift
def simulate_genetic_drift(population_size, generations, num_simulations):
    fixation_counts = np.zeros(generations)
    
    for sim in range(num_simulations):
        p = 0.5  # Starting frequency hai allele A ka
        for gen in range(generations):
            num_alleles_A = np.random.binomial(population_size, p)
            p = num_alleles_A / population_size
            if p == 0 or p == 1:
                fixation_counts[gen] += 1
                break
                
    fixation_probability = fixation_counts / num_simulations
    return fixation_probability

# Parameters or data dalna hai yahan par
population_size = 100
generations = 100
num_simulations = 1000

# Simulate genetic drift
fixation_prob = simulate_genetic_drift(population_size, generations, num_simulations)


plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
plt.plot(fixation_prob)
plt.xlabel('Generations')
plt.ylabel('Fixation Probability')
plt.title('Fixation Probability Over Generations')

# Histogram of fixation times
fixation_times = np.nonzero(fixation_prob)[0]
plt.subplot(1, 3, 2)
plt.hist(fixation_times, bins=30, color='green', edgecolor='black')
plt.xlabel('Fixation Time')
plt.ylabel('Frequency')
plt.title('Histogram of Fixation Times')

# Histogram of allele frequencies at fixation
allele_frequencies = np.random.binomial(population_size, 0.5, size=(num_simulations, generations)) / population_size
allele_frequencies_at_fixation = allele_frequencies[:, fixation_times[-1]]
plt.subplot(1, 3, 3)
plt.hist(allele_frequencies_at_fixation, bins=30, color='red', edgecolor='black')
plt.xlabel('Allele Frequency at Fixation')
plt.ylabel('Frequency')
plt.title('Allele Frequencies at Fixation')

plt.tight_layout()
plt.show()
