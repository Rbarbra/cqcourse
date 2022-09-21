user_input_1 = int(input("Type the length of your tuple 1: "))
user_input_2 = int(input("Type the length of your tuple 2: "))
user_input_3 = int(input("Type the length of your tuple 3: "))
user_input_4 = int(input("Type the length of your tuple 4: "))


tuple_1 = tuple(range(user_input_1))
tuple_2 = tuple(range(user_input_2))
tuple_3 = tuple(range(user_input_3))
tuple_4 = tuple(range(user_input_4))

print(f"tuple 1 has the content {tuple_1} and the size {user_input_1}")
print(f"tuple 2 has the content {tuple_2} and the size {user_input_2}")
print(f"tuple 3 has the content {tuple_3} and the size {user_input_3}")
print(f"tuple 4 has the content {tuple_4} and the size {user_input_4}")

#try to get an index of any  number from your list
user_number_1 = int(input("Type the number of the element in tuple 1: "))
user_number_2 = int(input("Type the number of the element in tuple 2: "))
user_number_3 = int(input("Type the number of the element in tuple 3: "))
user_number_4 = int(input("Type the number of the element in tuple 4: "))

user_index_1 = user_number_1 - 1
user_index_2 = user_number_2 - 1
user_index_3 = user_number_3 - 1
user_index_4 = user_number_4 - 1

#user_index_1 = tuple_1.index(user_number_1)
#user_index_2 = tuple_2.index(user_number_2)
#user_index_3 = tuple_3.index(user_number_3)
#user_index_4 = tuple_4.index(user_number_4)

print(f"At index {user_index_1} tuple 1 has the content {tuple_1[user_index_1]}")
#print(f"tuple 2 has the content {tuple_2} and the  {user_number_2}")
#print(f"tuple 3 has the content {tuple_3} and the  {user_number_3}")
#print(f"tuple 4 has the content {tuple_4} and the  {user_number_4}")
