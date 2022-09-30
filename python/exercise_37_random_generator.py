# write a program that generates several random numbers.
import random
#randnum_1 = random.randint(0,100)
#randnum_2 = random.random()
#randnum_3 = random.gauss(1,5)

int(input("Enter the first lowest number of your range one random number: "))
user_input_1_end = int(input("Enter the last highest number of your range  one random number:  "))
user_input_2_start = int(input("Enter the first lowest number of your range two random number: "))
user_input_2_end = int(input("Enter the last highest number of your range  two random number:  "))
ser_input_3_start = int(input("Enter the first lowest number of your range three random number: "))
user_input_3_end = int(input("Enter the last highest number of your range  three random number:  "))

user_input_1_start = random.randint(x)
user_input_1_end =  random.randint(a)
user_input_2_start = random.randint(y)
user_input_2_end = random.randint(c)
user_input_3_start = random.randint(b)
user_input_3_end = random.randint(k)


print(f"{user_input_1_start} for lowest number in the one range {x} ")
print(f"{user_input_1_end} for highest number in the one range {a} ")
print(f"{user_input_2_start} for lowest number in the two range {c,k}")
rint(f"{user_input_2_end} for highest number in the two range  {x,y} ")
print(f"{user_input_3_start} for the lowest number in the three range {a,b} ")
print(f"{user_input_3_end} for  the highest number in the three range {c,k}")
