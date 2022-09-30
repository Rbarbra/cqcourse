import numpy as np
#an array consisting of 25 zeros
array_1 = np.zeros(25)
#an array consisting of 8 ones
array_2 = np.ones(8)
#an array consisting of 24 numbers of my choice
#array_3 = np.arange(24),reshape(4,4)
array_3 = np.arange(24)

array_4 = np.zeros((4,6))

# a two dimensional arrays TD cosisting of 6 rows of arrays with 5 entries:
array_TD = np.random.randn(6,5)

#printing out all the arrays
print(array_1)
print(array_2)
print(array_3)
print(array_4)
print(array_TD)

#use the arrays from exercise 38 and run some mathematical functions:

array_3_log10 = np.log10(array_3)
print(f"log10: {array_3_log10}")

array_1_log10 = np.log10(array_1)
print(f"log10: {array_1_log10}")


array_2_log10 = np.log10(array_2)
print(f"log10: {array_2_log10}")

array_4_log10 = np.log10(array_4)
print(f"log10: {array_4_log10}")

array_TD_log10 = np.log10(array_TD)
print(f"log10: {array_TD_log10}")
