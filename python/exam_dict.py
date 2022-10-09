
"""Dictionaries
You have the following dictionary: sample_dict = {'a': 100, 'b': 200, 'c': 300}.
Write a simple if statements to check whether the key ‘b’ is in the dictionary or not.
 Both cases should contain a print out.
Write a second if statement to check if the value 150 is in the dictionary.
Given the nested dictionary below set the salary of Brad to 8500.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}} """

#writing a simple statement to check whether the key "b" is in the dictionary or not
sample_dict = {'a': 100, 'b': 200, 'c': 300}

#checking whether key b is in our sample dictionary
if "key_b" in sample_dict:
    print("you know the right key to your value! ")
else:
   print("you dont know the right key to your value!: ")
#chicking
value == 150
if value in sample_dict.values()

    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")

#changing values of key in sample_dict
D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

#D['emp3']['name'] = 'Brand'
sample_dict['emp3']['Salary'] = '8500'

print(sample_dict['emp3'])
# Prints {'name': 'Max', 'job': 'Janitor'}
