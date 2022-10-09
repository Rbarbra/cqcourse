"""Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number.
For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10).
The result should be printed out."""

user_number = int(input("Please enter the number: "))

i=0
for num in range(1, user_number + 1):
      i += num
print("Sum of numbers is: ", i)
