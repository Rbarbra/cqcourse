def sum_up(a,b):
    sum = a+b
    return sum

def sum_over(InputList):
    sum = 0
    for elem in InputList:
        sum = sum_up(sum,elem)
    return sum

Ls1 = list(range(10))
Ls2 = list(range(15))
Sum1 = sum_over(Ls1)
Sum2 = sum_over(Ls2)

print(Sum1)
print(Sum2)