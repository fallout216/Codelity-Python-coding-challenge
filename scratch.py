import numpy as np

dim = 20
np.random.seed (1)
rd = np.random.randint(dim)
print("the random index is %d." %(rd))

x = np.eye(dim)[rd]

print(x)