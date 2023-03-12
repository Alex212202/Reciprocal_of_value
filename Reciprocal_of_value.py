import numpy as np

np.random.seed(0)

values = np.random.randint(1, 10, size=5)
def compute_reciprocal(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0/values[i]
    return output

print(compute_reciprocal(values))