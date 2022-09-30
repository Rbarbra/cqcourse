Var1 = int(input("Number 1 of 2: "))
Var2 = int(input("Number 2 of 2: "))

if Var1 > Var2:
    print("Wow your numbers decrease!")
elif Var1 < Var2:
    print("Wow your numbers increase!")
elif Var1 == Var2:
    print("The same number, really?")

if Var1 >= Var2:
    print("Your numbers could be identical, not vcery creative")

if Var1 <= Var2:
    print("Your numbers could be identical, not vcery creative")
    
if Var1 != Var2:
    print("You know two different numbers. Good for you!")