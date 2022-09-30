import os

os.mkdir("OS")
os.makedirs("OS",exist_ok=True)
os.chdir("OS")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.rename("OS","New_OS")
os.chdir("New_OS")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.system("rmdir New_OS")