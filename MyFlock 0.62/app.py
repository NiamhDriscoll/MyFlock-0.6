from flask import Flask, render_template, redirect, url_for
import sqlite3
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/signup", methods=["POST"])
def signup():
    return render_template("signup.html")

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

def init_db():
    conn = sqlite3.connect("C:\\Users\\Niamh\\OneDrive\\Desktop\\MyFlock 0.6\\myflock.db")
    cur = conn.cursor()
    cur.execute (''' CREATE TABLE IF NOT EXISTS people
(username TEXT, email TEXT, password TEXT)''')

def insert(username, email, password):
    try: 
     conn = sqlite3.connect("C:\\Users\\Niamh\\OneDrive\\Desktop\\MyFlock 0.6\\myflock.db")
    cur = conn.cursor
    cur.execute("INSERT INTO people (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    finally:
    if cur:
        cur.close()
    if conn:
        conn.close 

if __name__ == '__main__':
    init_db()
    insert(username, email, password)
    app.run(debug=True)
 