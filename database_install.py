import sqlite3

print('Installing DB.')

#SQLite Database
conn = sqlite3.connect("plswat_database.db")
sql_cursor = conn.cursor()

sql_cursor.execute("""CREATE TABLE roles (Name) """)
sql_cursor.execute("""CREATE TABLE quotes (Name, quote) """)
sql_cursor.execute("""CREATE TABLE videos (Name, title, url) """)

sql_cursor.execute("INSERT INTO roles VALUES ('FFXIV')")
sql_cursor.execute("INSERT INTO roles VALUES ('BLU')")
sql_cursor.execute("INSERT INTO roles VALUES ('Animal Crossing')")
sql_cursor.execute("INSERT INTO roles VALUES ('Nintendo')")
sql_cursor.execute("INSERT INTO roles VALUES ('One Piece')")
sql_cursor.execute("INSERT INTO roles VALUES ('Genshin Impact')")
sql_cursor.execute("INSERT INTO roles VALUES ('Game News')")
sql_cursor.execute("INSERT INTO roles VALUES ('FFXIV News')")
sql_cursor.execute("INSERT INTO roles VALUES ('FFXIV Fashion Report')")
sql_cursor.execute("INSERT INTO roles VALUES ('FFXIV Spoiler')")
conn.commit()

# insert multiple records using the more secure "?" method
quotes = [('Cari', '"Ey Schlitzi, wenn du mich mehr heilen laesst, warum bist du dann immer noch unter mit?"'),
          ('Cari', '"Auli, du hast ein gruenes Icon." | Auel: "Was ist gruen und rot gemischt?" | Cari: "HURENSOHN?"'),
          ('Cari', 'Caripapa erneuert das Silikon in der Kueche. | Caripapa: "Habt ihr eine Maschine?" | Cari: "Maschine? Was ist eine Maschine?" | Friede: "DENNIS!"'),
          ('Salty', 'Nein ich brauch dich Auli. <:FeelsTsundereMan:592629004633374739>'),
          ('Salty', '"Sie (Cari) ist es nicht gewohnt mit \'nem gutem Heiler (Auli) zusammen zu spielen."'),
          ('Auel', '"Passt auf Feuerball auf!" - Auel stirbt an Feuerball'),
          ('Friede', '"Ich bin gut in Videospielen" - laeuft 2 Sekunden spaeter runter.'),
          ('Dennis', '"Wie ist das nochmal bei Omega-M und Omega-Respect?"')
          ]
sql_cursor.executemany("INSERT INTO quotes VALUES (?,?)", quotes)
conn.commit()


videos = [('uwu', 'UWU First Clear WAR POV by :plswat:', 'https://www.youtube.com/watch?v=fDywcPePe20'),
          ('uwu', 'UWU Kill, Auli gets delitad :plswat:', 'https://www.youtube.com/watch?v=m5WiDjd9zCI'),
          ('uwu', 'UWU Kill, Auli gets delitad No.2 :plswat:', 'https://discordapp.com/channels/550014264262262804/550769119302254602/761672877258309632'),
          ('ucob', '1st UCoB Clear GNB POV by :plswat: ', 'https://www.youtube.com/watch?v=ZfgylrblzN0'),
          ('ucob', '1st UCoB Clear AST POV by :plswat: ', 'https://www.youtube.com/watch?v=zKL7mdu28DM'),
          ('tea', 'TEA Reclear DRK POV by :plswat: ', 'https://www.youtube.com/watch?v=E_d6PMkwDVU')
          ]

sql_cursor.executemany("INSERT INTO videos VALUES (?,?,?)", videos)
conn.commit()

print('Done installing DB.')