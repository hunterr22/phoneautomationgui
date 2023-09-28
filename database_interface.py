import sqlite3


def insert(email, day):
    conn = sqlite3.connect("add_info.db")
    conn.execute('INSERT INTO ADD_INFO (EMAIL, DAY) '
                 'VALUES (?, ?)', (email, day))
    conn.commit()
    conn.close()


def info():
    con = sqlite3.connect('add_info.db')
    con.row_factory = sqlite3.Row
    rows = con.execute('SELECT * FROM ADD_INFO').fetchall()
    for row in rows:
        print(list(row))


def delete(email):
    con = sqlite3.connect('add_info.db')
    cursor = con.cursor()
    cursor.execute("DELETE FROM ADD_INFO WHERE email=(?);", [email])
    con.commit()
    cursor.close()



con = sqlite3.connect('add_info.db')
cursor = con.cursor()
cursor.execute("SELECT * from ADD_INFO")
print(cursor.fetchall())
con.close()

