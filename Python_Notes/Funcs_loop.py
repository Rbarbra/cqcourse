def sum_over(inputlist):
    result = 0
    for elem in inputlist:
        result += elem
    return result

list1 = list(range(10))
list2 = list(range(15))
sum1 = sum_over(list1)
sum2 = sum_over(list2)

print(sum1)
print(sum2)