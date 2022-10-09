""" add a string _method to your class, so that the contents of your objects can be printed out in a good manor"""
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
    #adding a string-method to my class gene, this is called a magic gene.it helps
    def __str_(self):
        printout = f"the following gene:{self.__Name} has {self.__Nr_nucleotide} Nr_nucleotide {self.__Nr_readingframe} __Nr_readingframe, {self._Nucleotide} Nucleotide, {self._Readingframe} Readingframe"
