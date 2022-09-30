#creating a program that uses default arguments in its function
def introduction(Name, Hallotext = "How are you today?"):
    print("what is your name?", "Iam", Name +  "Thanks" + Hallotext)

introduction("Barbra")
introduction("Richard", "How are you today?")
