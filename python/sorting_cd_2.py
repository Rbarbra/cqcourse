#Defining class CD with two attributes: genre and artist
class CD:
    def __init__(self, genre, artist):
        self.genre = genre
        self.artist = artist
    def __repr__(self):
        return f"CD: Genre: {self.genre} - Artist: {self.artist}\n"

pop_artist_1 = CD("pop", "kp1")
pop_artist_2 = CD("pop", "kp2")
pop_artist_3 = CD("pop", "kp3")

rock_artist_1 = CD("rock", "kr1")
rock_artist_2 = CD("rock", "kr2")
rock_artist_3 = CD("rock", "kr3")

hiphop_artist_1 = CD("hiphop", "kh1")
hiphop_artist_2 = CD("hiphop", "kh2")
hiphop_artist_3 = CD("hiphop", "kh3")

cd_collection = [hiphop_artist_2,pop_artist_1, pop_artist_3, pop_artist_2, rock_artist_2, rock_artist_1, rock_artist_3, hiphop_artist_1, hiphop_artist_3]
print(f"Unsorted list:\n {cd_collection}")

#Sorting the list using a lambda function which is set as parameter "key" for the list method "sort"
cd_collection.sort(key=lambda x: (x.genre, x.artist))
print("Sorted list:")
print(cd_collection)
