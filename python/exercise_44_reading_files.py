#read the second file from exercise 43,by using a generator method.
#first method of reading the file by reading the whole file
with open("writingfile.txt","r") as read_file:
    contents = read_file.read()
print(contents)
print(repr(contents))

#second method of reading a file line by line
with open("writingfile.txt","r") as read_file2:
    lines = read_file2.readlines()

print(lines)

#third method of reading a file using a generator( with for loop ) plus the sum of the values
with open("writingfile.txt","r") as read_file3:
    sum = 0
    for line in read_file3:
        print(line)
        print(repr(line))
        print(line.strip('\n'))
        sum = int(line) + sum
        print(sum)

print("Finished")
