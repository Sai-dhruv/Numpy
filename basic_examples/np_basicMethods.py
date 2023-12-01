import numpy as np

np1 = np.arange(10)
print(np1)

# Zeros
np2 = np.zeros(10)
print("Zeros :", np2)

# MultiDimensional Zeros
np3 = np.zeros((2, 10))
print(np3)

# Full
np4 = np.full(5, 6)
print("Full Example :", np4)

# Full Multi dimensional
np5 = np.full((2, 4), 6)
print("Full Multi dimensional : ", np5)

# convert python list to np Array
my_list = [0, 1, 2, 3, 667667, 5, 6, 7, 7]
print(" My list :", my_list)
np6 = np.array(my_list)
print("Convert my-list to numpy array :", np6)
print("Type :", type(np6))
print("print specified position :", np6[4])
