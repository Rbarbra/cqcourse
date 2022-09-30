fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = []
for x in fruits:
    if "a" in x:
        newlist1.append(x)

print(newlist1) 

newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

newlist3 = [x.upper() for x in fruits if "a" in x]
print(newlist3) 