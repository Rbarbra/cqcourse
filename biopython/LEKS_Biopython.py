"""Biopython
Write down the example syntax for the EInfo, ESearch, ESummary, EFetch and ELink
method as you did during your exercises. You can run all methods in one script."""

# First we import the Entrez module from Biopython
#import Bio.Entrez as ez
# To use the services of the Entrez system we have to specify an Email address.
#ez.email = ""

#writing example syntax for EInfo
#if we want to get infos from specific database for example from a protein.
#we can use the method and syntax below we put arguments db and protein database as shown below.

#with ez.einfo(db="protein") as query:
#    proteinDict = ez.read(query)

#print(proteinDict)
#print(proteinDict["DbInfo"].keys())
#print(proteinDict["DbInfo"]["FieldList"])
# the dictionary above seems complex. it is easier to loop over this dictionary
# and look at each key seperately.
#So the loop below loops over the different sub dictionaries which are part of this FieldList.

#for field in proteinDict["DbInfo"]["FieldList"]:
    #field in proteinDict["DbInfo"]["FieldList"]
    # Now we can print out the Name (an abbreviation), the FullName and the
    # description of each search field available to us.
    #print(field["Name"],field["FullName"],field["Description"])

#writing example syntax for ESearch
#searching for HIV in humans from nucleotide database

#with ez.esearch(db="nucleotide", term="HIV[Orgn] AND [Gene]", idtype="acc") as query:
#    record_nuc = ez.read(query)

#print(record_nuc["Count"])
#print(record_nuc["IdList"])

#Writing example syntax for ESummary
#I get my known ids i want to search for with ESummary
#id_list = ["BDI13046.1", 'BDI13023.1', 'BDI13022.1', 'BDI13018.1', 'BDI13017.1', 'BDI13016.1', 'BDI13015.1', 'BDI13011.1']
#I loop my list over so that i can use it in the ESummary then later i parse the
#XML string to create a list in a  dictionary


#for ids in id_list:
#    with ez.esummary(db="protein", id=ids) as handle:
#        record = ez.read(handle)

#    print("Journal info\nid:",record[0]["Id"],"\nTitle: ",record[0]["Title"])
#print(record)

#writing example syntax for EFetch
#from Bio import SeqIO
import Bio.Entrez as ez
ez.email = " "

#using Efetch to get our data from nucleotide database in XML string and then
#  we can use the Entrez-parser to create a dictionary
# out of this string.
#with ez.efetch(db="nucleotide", id="7040", retmode="xml") as handle:
#    record2 = ez.read(handle)

#print(record2[0]["GBSeq_definition"])
#print(record2[0]["GBSeq_source"])

#Writing example syntax for ELink, this helps to get crosslinks between databases.
#getting the crosslink for my id using ELink
nucleotide_id = 7040
record = ez.read(ez.elink(dbfrom="nucleotide", id=nucleotide_id))
print(record)
#we can access the list of these IDs with the help of the of indices and keys combination.
print(record[0]["LinkSetDb"][0]["Link"])
