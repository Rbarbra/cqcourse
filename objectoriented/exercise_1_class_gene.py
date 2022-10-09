class gene():
    def __init__(self, Name, Nr_nucleotide, Nr_readingframe, Nucleotide, Readingframe):
        self.__Name = Name
        self.__Nr_nucleotide =  Nr_nucleotide
        self.__Nr_readingframe =  Nr_readingframe
        self._Nucleotide = Nucleotide
        self._Readingframe = Readingframe

human_gene = gene("Human_gene1", 70, 4, 60, 50)
print(human_gene._Nucleotide)

print(human_gene._Readingframe)
