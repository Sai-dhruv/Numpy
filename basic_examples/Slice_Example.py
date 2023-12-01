import numpy as np

# Slicing numpy Arrays :
np7 = [2, 3, 4, 2, 56, 45, 23, 43, 12]
print("Slicing Example :", np7[2:6])
print("Start to ENd :", np7[::])
print("From something to Till End :", np7[5:])

# Slice a 2-d Array
np8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Slicing 2 dimensional Array :", np8[1,3] )
