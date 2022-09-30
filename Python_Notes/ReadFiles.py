with open("TestFile.txt","r") as read_file:
    contents = read_file.read()
print(contents)
print(repr(contents))

with open("TestFile.txt","r") as read_file2:
    lines = read_file2.readlines()

print(lines)

with open("TestFile.txt","r") as read_file3:
    for line in read_file3:
        print(line)
        print(repr(line))
        print(line.strip('\n'))
