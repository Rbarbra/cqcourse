print("Create your list of choice")
lenuser_list_1 = int(input("how long should your list 1 be: "))
lenuser_list_2 = int(input("how long should your list 2 be: "))
lenuser_list_3 = int(input("how long should your list 3 be: "))

list_1 = list(range(lenuser_list_1))
list_2 = list(range(lenuser_list_2))
list_3 = list(range(lenuser_list_3))

print(f"List 1: {list_1}")
print(f"List 2: {list_2}")
print(f"List 3: {list_3}")

#Adding an element to the list_1
element_to_add = int(input("Which element do you want to add to list 1?: "))
list_1.append(element_to_add)
print(f"Element {element_to_add} added to list 1: {list_1}")

#Removing an element from list 1
element_to_remove = int(input("Which element do you want to remove from list 1?: "))
if element_to_remove in list_1:
    list_1.remove(element_to_remove)
    print(f"Element {element_to_remove} is removed from list 1: {list_1}")
else:
    print(f"Element {element_to_remove} is not in list 1: {list_1}")

#Reverse the list_1
#Yes or No
should_list_1_be_reversed = input("Do you want to reverse list 1? Please enter Yes or No: ")
if should_list_1_be_reversed == "Yes" or should_list_1_be_reversed == "No":
    if should_list_1_be_reversed == "Yes":
        list_1.reverse()
        print(f"Reversed list 1: {list_1}")
else:
    print("You did not type Yes or No!")


# Sorting to ascending order
list_1_sort = input("Do you want to sort your list 1 in ascending order (type No or Yes)")
if list_1_sort == "Yes" or list_1_sort == "No":
    if list_1_sort == "Yes":
        list_1.sort()
        print(f"Ascending sorted list 1: {list_1}")

#searching for the index of an element
index_in_list_1_to_be_searched = int(input("Which index in list 1 do you want to know? Please enter the Number: "))
if index_in_list_1_to_be_searched in list_1:
    list_1.index(index_in_list_1_to_be_searched)
    print(f"Index {index_in_list_1_to_be_searched} is in list 1: {list_1}")
else:
    print(f"Index {index_in_list_1_to_be_searched} is not in list 1: {list_1}")
