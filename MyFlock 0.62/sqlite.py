import sqlite3
conn=sqlite3.connect("C:\\Users\\Niamh\\OneDrive\\Desktop\\MyFlock 0.6\\myflock.db")
cur=conn.cursor()
cur.execute (''' CREATE TABLE IF NOT EXISTS people
(username TEXT, email TEXT, password TEXT)''')
conn.commit()
cur.execute("INSERT INTO people ")
cur.close()
conn.close

