import Bio.Entrez as ez
import xml.etree.ElementTree as ET
ez.email = " "

with ez.efetch(db="nucleotide", id="NC_001802.1", retmode="xml") as handle:
    record2 = ET.parse(handle)

record2 = record2.getroot()
print(record2)
print(record2.tag)
print(record2[0].tag)
print(record2[0][0].tag)

for x in record2.findall("GBSeq"):
    print(x.find("GBSeq_definition").text),
    print(x.find("GBSeq_source").text)
    print(x.find("GBSeq_sequence").text)
