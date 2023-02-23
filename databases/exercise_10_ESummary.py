import Bio.Entrez as ez
ez.email = " "
#I get my known ids i want to search for with ESummary
id_list = ["BDI13046.1", 'BDI13023.1', 'BDI13022.1', 'BDI13018.1', 'BDI13017.1', 'BDI13016.1', 'BDI13015.1', 'BDI13011.1']
#I loop my list over so that i can use it in the ESummary then later i parse the
#XML string to create a list in a  dictionary


for ids in id_list:
    with ez.esummary(db="protein", id=ids) as handle:
        record = ez.read(handle)

    print("Journal info\nid:",record[0]["Id"],"\nTitle: ",record[0]["Title"])
print(record)
