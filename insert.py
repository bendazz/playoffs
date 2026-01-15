import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
query = """
    INSERT INTO teams (city,name)
    VALUES
    ("Buffalo","Bills"),
    ("Los Angeles","Rams"),
    ("Seattle","Seahawks"),
    ("Chicago","Bears"),
    ("New England", "Patriots"),
    ("Houston","Texans"),
    ("San Francisco", "Forty-Niners"),
    ("Denver","Broncos");

"""

cursor.execute(query)

conn.commit()

conn.close()