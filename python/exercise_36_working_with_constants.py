import math

pi = math.pi
euler = math.e
tau = math.tau

# Save the original user input as string to a variable
user_input_original_x = input("Enter the number x: ")
user_input_original_y = input("Enter number y: ")

# Cast the user input to integer
user_input_x = int(user_input_original_x)
user_input_y = int(user_input_original_y)

user_input_constant = input("Which constant should be used to multiply the user input? 'pi', 'e' or 'tau'?: ")

if user_input_constant == "pi":
    user_input_x = user_input_x * math.pi
    user_input_y = user_input_y * math.pi
elif user_input_constant == "e":
    user_input_x = user_input_x * math.e
    user_input_y = user_input_y * math.e
elif user_input_constant == "tau":
    user_input_x = user_input_x * math.tau
    user_input_y = user_input_y * math.tau
else:
    print("You did not enter 'pi', 'e' or 'tau'.")

result_1 = math.exp(user_input_x)
result_2 = math.exp(user_input_y)
result_3 = math.log(user_input_x)
result_4 = math.log(user_input_y,user_input_x)
result_5 = math.log2(user_input_x)
result_6 = math.log2(user_input_y)
result_7 = math.log10(user_input_x)
result_8 = math.log10(user_input_y)
result_9 = math.pow(user_input_x,user_input_y)
result_10 = math.cos(user_input_y)
result_12 = math.sin(user_input_x)
result_13 = math.tan(user_input_y)

if user_input_x < 0:
    result_14 = math.acos(user_input_x)
    print(result_14)

if user_input_y > -1 and user_input_y < 1:
    result_15 = math.asin(user_input_y)
    print(result_15)

result_16 = math.atan(float(user_input_y))

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)
print(result_7)
print(result_8)
print(result_9)
print(result_10)
print(result_12)
print(result_13)
print(result_16)
