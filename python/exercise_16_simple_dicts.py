dict_2 = {}
dict_2 = {
    "salt types":"sodium chloride",
    "bases of DNA":"cytosine",
    "4+4":8,
    "types of chemical reaction":"reversible",
    "types of bonds":"double bond",
    "proteins":"antibodies",
    "salt types":"sodium chloride",
    "bases of DNA":"cytosine",
    "types of chemical reaction":"reversible",
    "types of bonds":"double bond",
    "molecular weight":"three",
    "viruses":"HIV",
    "bacteria":"E.coli",
    "vectors":"snails,"}

print(dict_2)

#to add a new user entry
new_user_key_to_be_added = input("Which new key do you want to add to the dictionary: ")
new_user_value_to_be_added = input(f"Which new value do you want to add to the dictionary for key {new_user_key_to_be_added}?: ")

if new_user_key_to_be_added not in dict_2:
    dict_2[new_user_key_to_be_added] = new_user_value_to_be_added
else:
    print("you dont know the right key to your value!: ")

print(f"List after adding key and value: \n {dict_2}")

key_to_be_removed = input("Which key do you want to remove from dictionary?: ")

if key_to_be_removed in dict_2:
    del dict_2[key_to_be_removed]
else:
    print("you dont know the right key to your value!: ")

print(dict_2)
