#creating directories using
import os
print(os.getcwd())
os.mkdir("ospython1")

#creating a subdirectories
os.chdir("ospython1")
print(os.getcwd())

os.mkdir("osnotice1")
os.mkdir("osscience1")
os.mkdir("osmath1")
os.mkdir("osgenetics1")
os.mkdir("osbiology1")

#by using os.system("") you can execute linux commands
os.system("ls")

#creating files in the subdirectories of ospython
os.chdir("osnotice1")
print(os.getcwd())
os.system("touch data1.txt")

os.chdir("..")
os.chdir("osscience1")
print(os.getcwd())
os.system("touch data2.txt")

os.chdir("..")
os.chdir("osmath1")
print(os.getcwd())
os.system("touch data3.txt")

os.chdir("..")
os.chdir("osgenetics1")
print(os.getcwd())
os.system("touch data4.txt")

os.chdir("..")
os.chdir("osscience1")
print(os.getcwd())
os.system("touch data5.txt")
