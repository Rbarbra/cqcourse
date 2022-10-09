#creating_a_simple_dictionary
dict_1 = {}
dict_1["salt types"]="sodium chloride"
dict_1["bases of DNA"]="cytosine"
dict_1["3+5"]=8
print(dict_1)


#user putting in new entry
new_user_entry_to_be_added_1 = input("Which new key do you want to add to dict 1?: ")
new_user_entry_to_be_added_2 = input("Which new value do you want to add to dict 1?: ")

if new_user_entry_to_be_added_1 not in dict_1:
    dict_1[new_user_entry_to_be_added_1] = new_user_entry_to_be_added_2]
else:
    print("you dont know the right key to your value!: ")

print(dict_1)
