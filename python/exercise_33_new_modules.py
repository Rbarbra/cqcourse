#generate a random number between 0 and 99, use the library to find a module
#and a function for this task
user_input = int(input("Guess a random number between 0 and 3:\n"))

#guess a random number
import random
num = random.randint(0,3)
#genarate now a while loop that asks for a quess as long as the user didnt guess right.
while num != user_input:
    print("wrong number, please guess again")
    user_input = int(input("Guess a random number between 0 and 3:\n"))

#give hints to the user if the number is lower or higher than the random number
if user_input > num:
    print("your number is greater than the needed number! ")
if user_input < num:
    print("your number is greater than the needed number! ")
if user_input == num:
    print("you have the number and congratulations! ")
else:
    print("sorry you are unlucky this time! ")
