nextflow.enable.dsl = 2
params.out = "${launchDir}/output"
params.storedir = "${baseDir}/cache"
params.url = null

//downloading reference sequence
process downloadFiles{
    publishDir "${params.out}/fasta", mode: "copy", overwrite: true
    storeDir params.storedir

    
    output:
    path "*.fasta"
    """
#wget "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=M21012&rettype=fasta&retmode=text" -O M21012.fasta
#adapt"{params.out}/fasta" to get the referencefiles with folder containing the sequencefiles
#from NCBI
wget "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?db=nucleotide&report=fasta&id=MT649289.1&extrafeat=null&conwithfeat=on&hide-cdd=on"-O MT649289.1.fasta
"""
}

//combining files
process combineFastaFiles{
    publishDir "${params.out}/output", mode: "copy", overwrite: true
    storeDir params.storedir
    input:
        path inputfile
    output:
      path "combined.fasta"
    """
    cat ${launchDir}/fasta/*.fasta > combined.fasta
    """
}

//mafft files
process mafft{
    publishDir "${params.out}/output", mode: "copy", overwrite: true
    storeDir params.storedir
    container "https://depot.galaxyproject.org/singularity/mafft%3A7.221--0"
    input:
        path fastafiles
    output:
      path "mafft.fasta"
    """
    mafft ${fastafiles} > mafft.fasta
    """
}
//trimming and cleaning the sequences
process trimal{
    publishDir "${params.out}/output", mode: "copy", overwrite: true
    storeDir params.storedir
    container "https://depot.galaxyproject.org/singularity/trimal%3A1.4.1--h9f5acd7_6"
    input:
        path mafftfastafiles
    output:
      path "trimal.fasta", emit: trimmedfasta
      path "report.html", emit: report
    """
    trimal -in ${mafftfastafiles} -out trimal.fasta -automated1 -htmlout report.html
    """
}

workflow {
  RefSeqfasta_channel = downloadFiles()
  combinedfasta_channel = combineFastaFiles(RefSeqfasta_channel)
  Mafft_channel = mafft(combinedfasta_channel)
  //Trimal_channel = trimal(Mafft_channel)
  trimal(Mafft_channel)
}


















