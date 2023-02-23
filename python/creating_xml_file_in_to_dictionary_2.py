import xmltodict

with open("exericise_4_protein_structure.xml") as fd:
    doc = xmltodict.parse(fd.read())

print(doc)
print("")
print(doc["structural_proteins"])
print("")
print(doc["structural_proteins"]["immunglobulins"])
print("")
print(doc["structural_proteins"]["immunglobulins"]["immunglobulin_IgA"])
print(doc["structural_proteins"]["immunglobulins"]["immunglobulin_IgA"]["isoelectric_point"])
