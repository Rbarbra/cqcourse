integer1 = 2
integer2 = None
float1 = 3.5
float2 = None
string1 = "Hello"
string2 = None

list1 = [integer1,integer2,float1,float2,string1,string2]

print(integer1)
print(integer2)
print(float1)
print(float2)
print(string1)
print(string2)
print(list1)

for elem in list1:
    print(type(elem))
    if elem:
        print("Yes this is an element with the value",elem)
    else:
        print("No this is a NoneType")