try:
    number1 = int(input("Give me a number: "))
except ValueError:
    print("Hey I wanted a number")
    number1 = 100
else:
    print("Nice Number")
    
number2 = 100

try:
    result = number2 / number1
except ZeroDivisionError:
    print("This is mathematical bullshit")
else:
    print(result)
finally:
    print("We are finished")