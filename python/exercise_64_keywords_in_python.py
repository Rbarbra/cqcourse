list_1 = list(range(100))

#summing up the list
for elem in list_1:
    sum = 0
    sum = sum + elem
    print(elem)

    #second statement in my loop which passes the the loop
    if elem > 50:
        pass
    #statement in my loop that breaks the loop
    if elem == 60:
        break
    if elem > 40:
        continue
    print("End of loop")
