import xmltodict

with open("exercise_3_test_catalog.xml") as fd:
    doc = xmltodict.parse(fd.read())

print(doc)
print("")
print(doc["Experiments"])
print("")
print(doc["Experiments"]["Molecular_exp"])
print("")
print(doc["Experiments"]["Molecular_exp"][0])
print(doc["Experiments"]["Molecular_exp"][0]["Title"])
