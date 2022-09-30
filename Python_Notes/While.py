import random

Ls1 = list(range(100))
random.shuffle(Ls1)

i = 0
while Ls1[i] != 50:
    print("You didn't found the fifty")
    i += 1
    print("You ran",i,"iterations until now")

print("You found the fifty after",i,"iterations")

test = True
i = 0
sum = 0
while test:
    sum += list1[i]
    if sum > 2500:
        test = False
        print("You reached the Threshshold of:", sum)
    else:
        print(f"After {i+1} iterations your still under the Threshold")
    i += 1