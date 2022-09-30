# write a program that creates or writes two files
file = open("Introduction.txt","w")
file.write("My name is Barbra\n")
file.write("Iam studing Bioinformatics\n")
file.close()

#afterwords close the file and open it again and add another three lines of text to the file.
string1 = "i live in Germany"
string2 = ("Iam 37 years of age")
float1 = 344456.566

with open("Introduction.txt","a") as with_file:
    with_file.write(string1+"\n")
    with_file.write(string1+"\n")
    with_file.write(str(float1))

print("Finished")


with open("writingfile.txt","w") as with_file:
    for i in range(11):
        with_file.write(str(i)+"\n")
print("Finished")
