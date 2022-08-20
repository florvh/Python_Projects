import sqlite3

#connect met de database
conn = sqlite3.connect('Leden.db')

#maakt een cursor
c = conn.cursor()

#maakt een table
#c.execute("""CREATE TABLE Leden (
#    username text,
#    punten integer
#    )""")

#insert data in een table
#c.execute("INSERT INTO Leden VALUES ('CUM MONSTER', 69),('kade', 500000)")









#commit de commands
conn.commit()

#sluit de connection
conn.close()