list1 = [5,6,7,1,5,8]
list2 = []
list3 = [1,None,4]
if any(elem > 0 for elem in list1):
    print("Nice One")
    
if any(elem > 6 for elem in list1):
    print("At least one bigger number")

if any(elem > 10 for elem in list1):
    print("Hey a number with two digits")
    
print(any(list1))
print(any(list2))
print(any(list3))