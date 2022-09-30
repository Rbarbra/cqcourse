dictionary_proteins = {}
dictionary_proteins["antibodies"] = {"Name":"immunoglobulinIgG","Length":"10nm","function":"control infection","location":"blood"}
dictionary_proteins["enzymes"] = {"Name":"DNA polymerase","Length":"150bp","function":"DNA sequence","location":"cell"}
dictionary_proteins["hormones"] = {"Name":"prolactin","Length":"210ng/ml","function":"milk production","location":"pituitary gland" }
dictionary_proteins["structural"] = {"Name":"alpha helix","Length":"6bp","function":"help in sequence interaction in protein DNA","Location":"protein"}

print(dictionary_proteins)
print(dictionary_proteins["antibodies"])
print(dictionary_proteins["enzymes"])
print(dictionary_proteins["hormones"])
print(dictionary_proteins["structural"])

#Asking the user to add an entry,delete an entry orchanges an entry.
user_choice = input("Add,Delete or change")


if user_choice == "Add":
new_user_key_to_be_added = input("Which new key do you want to add to the dictionary: ")
new_user_value_to_be_added = input(f"Which new value do you want to add to the dictionary for key {new_user_key_to_be_added}?: ")

   if new_user_key_to_be_added not in dictionary_proteins:
   dictionary_proteins[new_user_key_to_be_added] = new_user_value_to_be_added

else:
    print("you dont know the right key to your value!: ")

print(f"List after adding key and value: \n {dictionary_proteins}")

#key to be removed
if user_choice = "Delete":
key_to_be_removed = input("Which key do you want to remove from dictionary?: ")

   if key_to_be_removed  in dictionary_proteins:
   del dictionary_proteins[key_to_be_removed]

else:
    print("you have to adjust your key well to fit in this dictionary!: ")

print(dictionary_proteins)

#changing any key in your dictionary
if user_choice == "change":
the_key_to_be_changed = input("Which key do you want to change?: ")
    dictionary_proteins(the_key_to_be_changed )
