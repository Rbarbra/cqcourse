user_input_1 = int(input("Please give the first number: "))
user_input_2 = int(input("Please give the second number: "))

sum_of_user_input_1_and_2 = user_input_1 + user_input_2

if sum_of_user_input_1_and_2 > 100:
    print("That is a big number")
elif sum_of_user_input_1_and_2 > 10:
    print("That is a mediocre number")
elif sum_of_user_input_1_and_2 > 5:
    print("That  is a small number")
else:
    print("That is a very small number")
