# user creating sets
user_input_1 = int(input("Type the length of your set 1: "))
user_input_2 = int(input("Type the length of your set 2: "))
user_input_3 = int(input("Type the length of your set 3: "))
user_input_4 = int(input("Type the length of your set 4: "))

#the user has to tell the length of the set
set_1 = set(range(user_input_1))
set_2 = set(range(user_input_2))
set_3 = set(range(user_input_3))
set_4 = set(range(user_input_4))

#printing the sets of the user
print(f"set 1 has the content {set_1} and the size {user_input_1}")
print(f"set 2 has the content {set_2} and the size {user_input_2}")
print(f"set 3 has the content {set_3} and the size {user_input_3}")
print(f"set 4 has the content {set_4} and the size {user_input_4}")
