import xml.etree.ElementTree as ET

mytree = ET.parse("exericise_4_protein_structure.xml")
myroot = mytree.getroot()

print(myroot)
print(len(myroot))
print(myroot.tag)

print(myroot[0].tag)
print(myroot[0][0].tag)
print(myroot[0][0][3].tag)
print(myroot[0][0][0].text)
print(myroot[0][0][0].attrib)
print(myroot[0][0][4].attrib["unit"])

for x in myroot.findall("immunglobulins"):
    structure = x[0].find("structure").text
    sequence = x[0].find("sequence").text
    print(structure,sequence)
