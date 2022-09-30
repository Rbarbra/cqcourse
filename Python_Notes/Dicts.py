Dict1 = {"Hello":"World","3+4":7,"5/2":2.5}

print(Dict1)

Dict1["9-3"] = 6
print(Dict1)

Dict1["Hello"] = "Hi"
print(Dict1)

del Dict1["3+4"]
print(Dict1)

if "Hello" in Dict1:
    print("Hey you know which keys you used for your dictionary")
else:
    print("You don't know the keys of your own dcitionary?")
    
print(list(Dict1.keys()))
print(list(Dict1.values()))