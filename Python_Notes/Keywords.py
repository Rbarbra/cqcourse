list1 = list(range(25))

for elem in list1:
    print(elem)
    if elem > 10:
        pass
    if elem == 20:
        break
    if elem > 15:
        continue
    print("End of Loop")