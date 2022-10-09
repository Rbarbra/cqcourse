"""You want to sort your CD collection, consisting of 250 CDs, according to genre and artist.
You have CDs of five different genres, Pop, Rock, Dance, Hip-Hop and Folk.
For each genre there are seven different artists (KP1 to KP7, KR1 to KR7, etc…).
 Write the Pseudocode and create a structogram for
this problem. Don’t forget to define possible additional variables."""

#sorting them according to the dictionary
#if my dictinary genres contains a subdictionary artists

#creating a dictinary called genres
dict_genre = {}
dict_genre["artists"] = {"pop":["KPI", "KP2", "KP3", "KP4", "KP5", "KP6", "KP7"]}
dict_genre["artists"] = {"rock":["KRI", "KR2", "KR3", "KR4", "KR5", "KR6", "KR7"]}
dict_genre["artists"] = {"dance":["KDI", "KD2", "KD3", "KD4", "KD5", "KD6", "KD7"]}
dict_genre["artists"] = {"hip_hop":["KHI", "KH2", "KH3", "KH4", "KH5", "KH6", "KH7"]}
dict_genre["artists"] = {"folk":["KFI", "KF2", "KF3", "KF4", "KF5", "KF6", "KF7"]}
print(dict_genre)
print(dict_genre["artists"])
print(dict_genre["artists"])
print(dict_genre["artists"])
print(dict_genre["artists"])
print(dict_genre["artists"])

#if the total number of cds is 250 cds how can one pick a cd of choice
#if cd to be picked is == to cd0 and our range is 1 to 250.
#getting a cd in from a collection of CDs
#looping over the lists of cds
#cd runs from 0 to 249
for cd in list(range(250)):
    print(cd)
