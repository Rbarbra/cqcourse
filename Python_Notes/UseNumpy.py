import numpy as np

Array1 = np.array([4,3,2,1])
Array2 = np.arange(4)
Array3 = np.zeros(4)
Array4 = np.ones(4)
Array5 = np.zeros((3,4))
Array6 = np.arange(15).reshape(3, 5)
Array7 = np.random.randn(6,4)

print(Array1)
print(Array2)
print(Array3)
print(Array4)
print(Array5)
print(Array6)
print(Array7)

print(Array1.sum())
print(Array1.min())
print(Array1.max())

print(Array7.sum())
print(Array7.min())
print(Array7.max())

print(Array7.transpose())
print(Array7.shape)

Array8 = Array1 * 4
print(Array8)
Array9 = Array8 - 2
print(Array9)
Array10 = Array7 * 5
print(Array10)