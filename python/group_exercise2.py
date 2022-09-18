print("Please enter 6 numbers.")
user_input_1 = int(input("Enter number 1 of 6: "))
user_input_2 = int(input("Enter number 2 of 6: "))
user_input_3 = int(input("Enter number 3 of 6 "))
user_input_4 = int(input("Enter number 4 of 6: "))
user_input_5 = int(input("Enter number 5 of 6: "))
user_input_6 = int(input("Enter number 6 of 6: "))

print("Which of the mathematical Operations you want to use?")
print("Addition, Subtraction, Multiplication or Division?")

#Contains the operation which the user has given
mathematical_operation = input("Please enter now the mathematical Operation: ")

result = None
if mathematical_operation == "Addition":
    result = user_input_1 + user_input_2 + user_input_3 + user_input_4 + user_input_5 + user_input_6
    print(f"The result is {result}.")
elif mathematical_operation == "Subtraction":
    result = user_input_1 - user_input_2 - user_input_3 - user_input_4 - user_input_5 - user_input_6
    print(f"The result is {result}.")
elif mathematical_operation == "Multiplication": # with quotation marks because iam comparing with string values.
    result = user_input_1 * user_input_2 * user_input_3 * user_input_4 * user_input_5 * user_input_6
    print(f"The result is {result}.")
elif mathematical_operation == "Division":
    result = user_input_1 / user_input_2 / user_input_3 / user_input_4 / user_input_5 / user_input_6
    print(f"The result is {result}.")
else:
    print("Wrong operation")
