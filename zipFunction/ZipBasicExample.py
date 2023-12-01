import numpy as np

def zipExample():
	a= np.array([10,20,30])
	b= np.array([1,2,3])
	for m,n in zip(a,b):
		print(m*n)

zipExample()
