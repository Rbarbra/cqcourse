string1 = "Hello Christoph"
float1 = 456.34

file = open("TestFile.txt","w")
file.write("My name is Christoph\n")
file.write("Hello World\n")
file.write(string1)
file.write(str(float1))
file.close()

with open("TestFile2.txt","w") as with_file:
    with_file.write("This is a test Test\n")
    with_file.write(string1)
    with_file.write(str(float))
