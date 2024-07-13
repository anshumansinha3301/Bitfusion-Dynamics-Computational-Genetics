import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load gene expression data (example data)
# For demonstration, generate synthetic data
np.random.seed(0)
genes = [f'Gene_{i}' for i in range(1, 101)]
samples = [f'Sample_{i}' for i in range(1, 21)]
data = np.random.normal(loc=10, scale=2, size=(100, 20))


df = pd.DataFrame(data, index=genes, columns=samples)


mean_expression = df.mean(axis=1)
std_expression = df.std(axis=1)


plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
sns.heatmap(df, cmap='viridis', cbar=True)
plt.title('Gene Expression Heatmap')

plt.subplot(1, 3, 2)
plt.hist(mean_expression, bins=30, color='blue', edgecolor='black')
plt.xlabel('Mean Expression Level')
plt.ylabel('Frequency')
plt.title('Distribution of Mean Gene Expression')

plt.subplot(1, 3, 3)
plt.scatter(mean_expression, std_expression, color='red')
plt.xlabel('Mean Expression Level')
plt.ylabel('Standard Deviation')
plt.title('Mean vs. Standard Deviation of Gene Expression')

plt.tight_layout()
plt.show()
