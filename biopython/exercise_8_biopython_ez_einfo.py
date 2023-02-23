import Bio.Entrez as ez
ez.email = ""

#with ez.einfo() as query:
    #xml_string = query.read()
#print(xml_string)

with ez.einfo() as query:
    parse_dict = ez.read(query)
print(parse_dict)
print(parse_dict)["Dblist"]

#searching for pubmed database

with ez.einfo(db="pubmed") as query:
    pubmedDict = ez.read(query)

print(pubmedDict)
#print(pubmedDict["DbInfo"].keys())
print(pubmedDict["DbInfo"]["FieldList"])

#searching for protein database
with ez.einfo() as query:
    parse_dict = ez.read(query)
print(parse_dict)
#print(parse_dict)["Dblist"]

with ez.einfo(db="protein") as query:
    proteinDict = ez.read(query)

print(proteinDict)
#print(proteinDict["DbInfo"].keys())
print(proteinDict["DbInfo"]["FieldList"])
