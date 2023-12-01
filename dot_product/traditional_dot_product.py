import numpy as np
a = np.array([10,20,30])
b = np.array([100,200,300])
result = 0
for m,n in zip(a,b):
	result = result+m*n
print("Dot product is ",result)
