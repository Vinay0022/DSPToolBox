import numpy as np
  
# Creating two numpy One-Dimensional
# array using the array() method
arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([4,1,1,2]
arr2 = np.array([1,2,2,1])
  
# Display the arrays
print("Array1:->\n", arr1)
print("\nArray2:->\n", arr2)
  
# Check the Dimensions of both the arrays
print("\nDimensions of Array1:->\n", arr1.ndim)
print("\nDimensions of Array2:->\n", arr2.ndim)
  
# Check the Shape of both the arrays
print("\nShape of Array1:->\n", arr1.shape)
print("\nShape of Array2:->\n", arr2.shape)
  
# To return the discrete linear convolution
# of two one-dimensional sequences,
# use the numpy.convolve() method in Python Numpy
print("\nResult:->\n", np.convolve(arr1, arr2))