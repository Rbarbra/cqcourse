# Exercise14 - A Pipeline
from Bio import SeqIO
import Bio.Entrez as ez
ez.email = "christoph-knorr@gmx.de"

term = "Varicella-zoster virus"
id_collection = {}
sequence_collection = {"Protein":{},"Nucleotide":{}}

with ez.esearch(db="pubmed", term=term) as query:
    record_pub = ez.read(query)
id_collection["PubMed"] = record_pub["IdList"]

with ez.esearch(db="nucleotide", term=term) as query:
    record_nuc = ez.read(query)
id_collection["Nucleotide"] = record_nuc["IdList"]

with ez.esearch(db="protein", term=term) as query:
    record_prot = ez.read(query)
id_collection["Protein"] = record_prot["IdList"]

for id in id_collection["Nucleotide"]:
    with ez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text") as handle:
        record = SeqIO.read(handle, "fasta")
    sequence_collection["Nucleotide"][id] = record.seq

for id in id_collection["Protein"]:
    with ez.efetch(db="protein", id=id, rettype="fasta", retmode="text") as handle:
        record = SeqIO.read(handle, "fasta")
    sequence_collection["Protein"][id] = record.seq

print(sequence_collection)
