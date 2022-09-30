# write a simple  python program that generates different arrays:
import numpy as np
#an array consisting of 25 zeros
array_1 = np.zeros(25)
#an array consisting of 8 ones
array_2 = np.ones(8)
#an array consisting of 24 numbers of my choice
#array_3 = np.arange(24),reshape(4,4)
array_3 = np.arange(24)

# a two dimensional arrays TD cosisting of 6 rows of arrays with 5 entries:
array_TD = np.random.randn(6,5)

#printing out all the arrays
print(array_1)
print(array_2)
print(array_3)
print(array_TD)

print(array_1.sum())
print(array_1.min())
print(array_1.max())
print(array_1.transpose())
print(array_1.shape)

print(array_2.sum())
print(array_2.min())
print(array_2.max())
print(array_2.transpose())
print(array_2.shape)

print(array_3.sum())
print(array_3.min())
print(array_3.max())
print(array_3.transpose())
print(array_3.shape)

print(array_TD.sum())
print(array_TD.min())
print(array_TD.max())
print(array_TD.transpose())
print(array_TD.shape)
