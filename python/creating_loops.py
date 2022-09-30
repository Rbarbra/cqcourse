#create the list
loop_list = list(range(30))
#print(loop_list)

#then print your loop list with help of loop function
for i in range(30):
    print(i)

# another loop process that sums up all numbers in the setted range
sum = 0
for i in range(30):
    sum = sum + i
    #sum++

print(f"Sum all numbers from 0 to 29: {sum}")

# another loop process that sums up  all the even numbers in the setted range
for i in range(0,30,2):
    #Check for even number
    sum = sum + i

print(f"sum for all even numbers: {sum}")


reversed_list = []

for i in reversed(loop_list):
    reversed_list.append(i)

print(f"Reversed list: {reversed_list}")
