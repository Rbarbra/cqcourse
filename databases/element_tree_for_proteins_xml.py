import xml.etree.ElementTree as ET

mytree = ET.parse("proteins.xml")
myroot = mytree.getroot()

print(myroot)
print(len(myroot))
print(myroot.tag)

print(myroot[0].tag)
print(myroot[0][0].tag)
print(myroot[0][2][0].tag)
print(myroot[0][3][0].text)
print(myroot[0][0][0].attrib)
print(myroot[0][0][4].attrib["unit"])

for x in myroot.findall("protein"):
    names = x[0].find("names").text
    SSEs = x[0].find("SSEs").text
    print(structure,sequence)
