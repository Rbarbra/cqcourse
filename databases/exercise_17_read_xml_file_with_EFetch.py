import xmltodict
import Bio.Entrez as ez
# set email
ez.email = " "
#reading in the files got by EFetch inform of a dictionary
#with ez.efetch(db="nucleotide", id="3309", retmode="xml") as handle:
#    record2 = xmltodict.parse(handle)

#print(record2)
#print(record2["GBSet"]["GBSeq"]["GBSeq_definition"])
#print(record2["GBSet"]["GBSeq"]["GBSeq_source"])
#print(record2["GBSet"]["GBSeq"]["GBSeq_sequence"])

#reading in the files got by EFetch about the HIV VIRUS in form of a dictionary
with ez.efetch(db="nucleotide", id="NC_001802.1", retmode="xml") as handle:
    record2 = xmltodict.parse(handle)

print(record2)
print(record2["GBSet"]["GBSeq"]["GBSeq_definition"])
print(record2["GBSet"]["GBSeq"]["GBSeq_source"])
print(record2["GBSet"]["GBSeq"]["GBSeq_sequence"])
