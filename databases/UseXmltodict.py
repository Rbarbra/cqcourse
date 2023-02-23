"""
This is the example script for parsing XML files using xmltodict. This module
creates adictionary out of our XML file and allows us to access the data by
moving through a complex nested dictionary
"""
# First we have to import our module
import xmltodict
# Now we can read in and parse our file. To do this we have to work by using a
# with statement similiar to the ones we saw when working with files in Python.
# Here we don't need to specify what we want to do with the file. Don't forget
# to use an alias for your file (here: fd).
with open('Music.xml') as fd:
    # Now we can read in and parse our file. We have to use the read() function
    # which allows us to read in the contents of our file as one big string and
    # than we hand over this string to the parser of our module xmltodict. This
    # parser takes the string and creates a dictionary out of it which we can
    # assign a name of our choice (here: doc)
    doc = xmltodict.parse(fd.read())
# Now we can look at our dictionary and move through it by chaining together
# keys and indices depending on the hierarchy in our file. If you have the
# chance look at your xml file in parallel, since it easier to understand the
# hierarchy of the data in these files. First we print out our whole dicitonary
print(doc)
print("")
# Now We print ou tthe value assinged to the most outer tag (track)
print(doc["tracks"])
print("")
# Now we print out the value assigned to the second most outer tag (track) which
# is a list since it appears multiple times in our XML file.
print(doc["tracks"]["track"])
print("")
# Now we can access the dictionaries in this list with the help of indices
print(doc["tracks"]["track"][0])
print("")
# Last but not Least we can use the key of this dictionary in our list to
# access a specific value of our song
print(doc["tracks"]["track"][0]["title"])
# There is a module called pprint (short for pretty print) that is maybe helpful
# for printing out dictionaries in a better way. You can use it as shown below
# by importing it and than using the pprint() function of the module pprint()
# instead of a normal print()
import pprint
pprint.pprint(doc)
