#write a program that takes the name of a file from the user and generate a copy of the file.
user_file_name = input("Enter the name of your file: ")
#creating the file
with open("user_file_name","w") as user_file_name:
    user_file_name.write("string1\n")
    user_file_name.write("string2\n")
    user_file_name.write(str("string3"))

print("Finished")

#use a generator to copy the content of the original file in to a new file line by line
with open(user_file_name,"r") as original_file:
    with open("copy_user_file_name","w") as copy_user_file_name:
        for line in original_file:
            copy_user_file_name.write(line)

print(copy_user_file_name)
