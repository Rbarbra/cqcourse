list_A = list(range(10,40))
print(list_A)

print("Check the Entry of your choice from the list A: ")
user_check_1 = int(input("Which entry do you want to check from the list A: "))
user_check_2 = int(input("Which entry do you want to check from list A: "))
user_check_3 = int(input("Which entry do you want to remove for list A: "))

print(user_check_1)
print(user_check_2)
print(user_check_3)

if user_check_1 in list_A:
    print(f"If user_check_1 is your in {list_A}: That is really clever!")
else:
    print(f"{user_check_1} is not in your {list_A}: That is not good!")

if user_check_2 in list_A:
    print(f"If {user_check_2} is your in {list_A}: That is really cool!")
else:
    print(f"{user_check_2} is not in your {list_A}: That is bad!")

    if user_check_3 in list_A:
        print(f"If {user_check_3} is in your {list_A}: That is really smart!")
    else:
        print(f"{user_check_3} is not in your {list_A}: Today is not your lucky Day!")
