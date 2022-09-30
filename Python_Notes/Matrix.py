matrix1 = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
matrix2 = [list(range(5)), list(range(5))]
matrix3 = [list(range(4))] * 8

print(matrix1)
print("")
print(matrix2)
print("")
print(matrix3)
print("")

matrix1[1][0] = 15
matrix2[0][4] = 100
matrix3[6][1] = 25

print(matrix1)
print("")
print(matrix2)
print("")
print(matrix3)
