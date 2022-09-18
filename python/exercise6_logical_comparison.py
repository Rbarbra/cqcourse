user_input1 = int(input("Please give me the first number: "))
user_input2 = int(input("Please give me the second number: "))
user_input3 = int(input("Please give me the third number: "))
user_input4 = int(input("Please give me the fourth number: "))

if (user_input1 == user_input2 and user_input3 == user_input4 or
user_input1 == user_input3 and user_input2 == user_input4 or
user_input1 == user_input4 and user_input2 == user_input3):
    print("Bravo, good logic thinking!")

else:
    print("Well you better think logically!")
