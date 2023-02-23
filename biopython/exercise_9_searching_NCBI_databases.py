import Bio.Entrez as ez
ez.email = ""

#seaching pubmed database for a term biopython in all articles with biopython in the tittle
#with ez.esearch(db="pubmed", term="biopython[title]", retmax="40" ) as query:
    #record_pub = ez.read(query)

#if "19304878" in record_pub["IdList"]:
#    print("Your article was found")
#seaching in nucleotide
#with ez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", idtype="acc") as query:
#    record_nuc = ez.read(query)


#print(record_nuc["Count"])
#print(record_nuc["IdList"])

#searching information about HIV
#with ez.esearch(db="nucleotide", term="HIV[Orgn] AND [Gene]", idtype="acc") as query:
#    record_nuc = ez.read(query)


#print(record_nuc["Count"])
#print(record_nuc["IdList"])

#searching for  Coxsackievirus
#with ez.esearch(db="nucleotide", term="Coxsackievirus A16[Title]", idtype="acc") as query:
#    record_nuc = ez.read(query)


#print(record_nuc["Count"])
#print(record_nuc["IdList"])

#searching in a protein databases
#with ez.esearch(db="protein", term="Coxsackievirus A16[Title]", idtype="acc") as query:
#    record_prot = ez.read(query)


#print(record_prot["Count"])
#print(record_prot["IdList"])
