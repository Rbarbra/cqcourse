input_number1 = int(input("Number 1 of 4: "))
input_number2 = int(input("Number 2 of 4: "))
input_number3 = int(input("Number 3 of 4: "))
input_number4 = int(input("Number 4 of 4: "))

if input_number1 == input_number2:
    print("Your first two numbers are identical, Wow")
    if input_number3 == input_number4:
        print("Your numbers three and four are also identical")

if input_number1 == input_number2 and input_number3 == input_number4:
    print("Twice, the same number really?")
