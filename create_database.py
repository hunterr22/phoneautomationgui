import sqlite3

conn = sqlite3.connect('add_info.db')
query = (''' CREATE TABLE ADD_INFO
        (EMAIL CHAR(50) NOT NULL,
        DAY TEXT NOT NULL
        );
''')

conn.execute(query)
conn.close()
