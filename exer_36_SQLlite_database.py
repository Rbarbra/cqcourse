import sqlite3
db = sqlite3.connect("mydatabase.db")
cur = db.cursor()
cur.execute('DROP TABLE IF EXISTS Student2')
cur.execute('''CREATE TABLE Student2 (ID int NOT NULL PRIMARY KEY, FirstName varchar(255), LastName varchar(255), Gender varchar(225), Nationality varchar(255), Flat_ID int NOT NULL, Housenumber int)''')
cur.execute("""INSERT INTO Student2 VALUES (15, "Silas","Rinner","Male", "German", 60, 70)""")
cur.execute("""INSERT INTO Student2 VALUES (1,"Sam", "Mukasa", "Male","Ugandan", 40, 50)""")
cur.execute("""INSERT INTO Student2 VALUES (3,"Patrik", "Menscher", "Male","German", 42, 52)""")
cur.execute("""INSERT INTO Student2 VALUES (4,"Peter", "Mark", "Male","USA", 43, NULL)""")
cur.execute("""INSERT INTO Student2 VALUES (5,"Samuel", "Peyiye", "Male","Brazil", 40, NULL)""")
cur.execute("""INSERT INTO Student2 VALUES (6,"Lucy", "kipplet", "Female","Kenya", 44, NULL)""")
cur.execute("""INSERT INTO Student2 VALUES (7,"Hope", "Smith", "Female","USA", 45, 53)""")
cur.execute("""INSERT INTO Student2 VALUES (9,"Jude", "Smith", "Female","USA", 47, 58)""")
cur.execute("""INSERT INTO Student2 VALUES (10,"Klarissa", "Wolf", "Female","German", 49, 59)""")
cur.execute("""INSERT INTO Student2 VALUES (11,"Mable", "Atemo", "Female","Uganda", 50, 60)""")

for row in cur.execute('SELECT * FROM Student2'):
    print(row)
    print(row[2])
print()
#exercise 40 selections
rows = cur.execute('SELECT * FROM Student2')
names = [description[0] for description in rows.description]
print(names)
rows = cur.fetchall()
for row in rows:
    print(row)

#db.commit()
#db.close()
