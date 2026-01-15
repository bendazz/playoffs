import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
query = """
    DELETE FROM TEAMS where id > 8;

"""

cursor.execute(query)

conn.commit()

conn.close()