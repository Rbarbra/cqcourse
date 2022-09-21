list_1 = list(range(0,40,))
list_2 = list(range(5,40,5))
list_3 = list(range(10,40,2))

print("print out the list: ")
print(list_1)
print(list_2)
print(list_3)

print("Which position do you want to insert your index on the lists and which number do you want to Insert: ")
user_index_1 = int(input("Insert your index on list 1: "))
user_number_1 = int(input("Insert the Number on the list 1: ") )
user_index_2 = int(input("Insert your index on list 2: "))
user_number_2 = int(input("Insert the Number on the list 2: "))
user_index_3 = int(input("Insert your index on list 3: "))
user_number_3 = int(input("Insert the Number on the list 3: "))

list_1.insert(user_index_1, user_number_1)
print(f"List 1 after inserting {user_number_1} at index {user_index_1}: {list_1}")

list_2.insert(user_index_2, user_number_2)
print(f"List 1 after inserting {user_number_2} at index {user_index_2}: {list_2}")

list_3.insert(user_index_3, user_number_3)
print(f"List 1 after inserting {user_number_3} at index {user_index_3}: {list_3}")
