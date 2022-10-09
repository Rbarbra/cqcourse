"""Expand the class from the first exercises by adding several methods to it"""
#using a one getter()method foe each attributes defined in the class Class

class gene():
    def __init__(self, Name, Nr_nucleotide, Nr_readingframe, Nucleotide, Readingframe):
        self.__Name = Name  #private
        self.__Nr_nucleotide =  Nr_nucleotide    #private
        self.__Nr_readingframe =  Nr_readingframe   #private
        self._Nucleotide = Nucleotide        #protected
        self._Readingframe = Readingframe   #protected



        #getter for name
    def get_Name(self):
        return self.__Name

    #getter for Nr_nucleotide
    def get_Nr_nucleotide(self):
        return self.__Nr_nucleotide

    #getter for Nr.reagingframe
    def get_Nr_readingframe(self):
        return self.__Nr_readingframe

    #getter for Nucleotide
    def get_Nucleotide(self):
        return self._Nucleotide

    #getter for _Readingframe
    def get_Readingframe(self):
        return self._Readingframe

    #the methods up_nucleotide(),down_nucleotide
    #getter for up_nucleotide
    def up_Nucleotide(self):
        self._Nucleotide += 60

    #getter for down_Nucleotide
    def down_Nucleotide(self):
        self._Nucleotide -= 60

    #getter for up_Readingframe
    def up_Readingframe(self,add):
        self._Readingframe += add

    #getter for down_Reading(self,add)
    def down_Readingframe(self,add):
        self._Readingframe -= add

     #print_state for all the getters
    def print_state(self, Name, Nr_nucleotide, Nr_readingframe, Nucleotide, Readingframe):
        print()

#generating an object from above
human_gene = gene("Human_gene1", 70, 4, 60, 50)
print(human_gene.get_Name())
print(human_gene.get_Nr_nucleotide())
print(human_gene.get_Nr_readingframe())
print(human_gene.get_Nucleotide())
print(human_gene.get_Readingframe())
