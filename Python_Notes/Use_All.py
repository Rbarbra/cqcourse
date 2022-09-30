list1 = [5,6,7,1,5,8]
list2 = []
list3 = [1,None,4]
if all(elem > 0 for elem in list1):
    print("Nice One")
    
if all(elem > 6 for elem in list1):
    print("At least one bigger number")

if all(elem > 10 for elem in list1):
    print("Hey a number with two digits")
    
print(all(list1))
print(all(list2))
print(all(list3))
