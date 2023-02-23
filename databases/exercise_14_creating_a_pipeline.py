#creating a pipeline that gives access to data of one ogranisms from different databases.
import Bio.Entrez as ez
ez.email = " "

# creating an HIV Pipeline
term = "HIV"
id_collection = "20348614","19187693" "14626050","2700293","8955040"
sequence_collection = {"Protein":{},"Nucleotide":{}}

#with ez.esearch(db="pubmed", term=term) as query:
#    record_pub = ez.read(query)
#id_collection["PubMed"] = record_pub["IdList"]

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
