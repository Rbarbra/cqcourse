from Bio import SeqIO
import Bio.Entrez as ez
ez.email = " "
#fetching data from protein database
#method one
#handle = ez.efetch(db="protein", id="BDI13011", rettype="gb", retmode="text")
#print(handle.read())

#method2
#with ez.efetch(db="protein", id="BDI13011", rettype="gb", retmode="text") as handle:
#    record1 = SeqIO.read(handle, "genbank")
#print(record1.id)
#method3
#with ez.efetch(db="protein", id="BDI13011", retmode="xml") as handle:
#    record2 = ez.read(handle)

#print(record2[0]["GBSeq_definition"])
#print(record2[0]["GBSeq_source"])

#fetching  data from nucleotide database.for HIV ID7040
#method one
#handle = ez.efetch(db="nucleotide", id="7040", rettype="gb", retmode="text")
#print(handle.read())
#method2
with ez.efetch(db="nucleotide", id="7040", rettype="gb", retmode="text") as handle:
    record1 = SeqIO.read(handle, "genebank")
print(record1.id)

#method3
#with ez.efetch(db="nucleotide", id="7040", retmode="xml") as handle:
#    record2 = ez.read(handle)

#print(record2[0]["GBSeq_definition"])
#print(record2[0]["GBSeq_source"])
