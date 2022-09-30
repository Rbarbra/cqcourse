try:
    input1  = int(input("Your number? "))
    if input1 not in [1,2,3,4,5]:
        raise RuntimeError
except RuntimeError:
    print("Input outside of range")
