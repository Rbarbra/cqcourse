import random

number = int(input("Please type in a number: "))
while number != 8:
    print("Wrong choice")
    number = int(input("Try again: "))

sum1 = 1
while sum1 < 1000:
    sum1 += sum1

list1 = list(range(101))
random.shuffle(list1)

i = 0
while list1[i] != 50:
    print(f"We are in iteration {i+1} and 50 wasn't found yet")
    i += 1

for elem in list1:
    if elem != 50:
        print("We didn't find the fifty yet")
    else:
        break
