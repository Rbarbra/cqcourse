Var1 = int(input("Type in a number: "))
Var2 = input("Now I need a string: ")

if Var1 > 10:
    print("Your input was greater than 10")
else:
    print("A pretty small number")
    
if Var2 == "Hello":
    print("How uncreative")
else:
    print("we are a Clown, aren't we")
    
if Var1 > 999:
    print("You really like big numbers, don't you?")
elif Var1 > 99:
    print("Still in the triple digits, nice choice")
elif Var1 >= 10:
    print("Only two digits, this poor poor number")
else:
    print("A single digit, I'm sorry for your number")