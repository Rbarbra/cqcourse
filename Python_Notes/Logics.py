Var1 = int(input("Number 1 of 4: "))
Var2 = int(input("Number 2 of 4: "))
Var3 = int(input("Number 3 of 4: "))
Var4 = int(input("Number 4 of 4: "))

if Var1 == Var2 and Var3 == Var4:
    print("Twice, the same number really?")

if Var1 == Var2 or Var3 == Var4:
    print("At least one duplicate number, you aren't creative, are you?")