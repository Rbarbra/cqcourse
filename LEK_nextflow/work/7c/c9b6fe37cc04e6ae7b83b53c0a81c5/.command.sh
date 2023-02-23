#!/bin/bash -ue
wget "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=M21012&rettype=fasta&retmode=text" -O M21012.fasta
# adapt"{params.out}/fasta" to connect the referencefiles with folder containing the sequencefiles
