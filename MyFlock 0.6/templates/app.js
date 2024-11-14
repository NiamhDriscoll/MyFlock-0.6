const { Database } = require('sqlite3');

const sqlite3 = require('sqlite3').verbose();

let usernameset = document.getElementById(username).value;
let emailset = document.getElementById(email).value;
let passwordset = document.getElementById(password).value;

let db = new sqlite3.Database('./myflock.db', sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, (err) => {
    if (err) {
        console.error(err.message);
    }
console.log("Connected to Database")})
db.run("CREATE TABLE IF NOT EXISTS people(username TEXT UNIQUE, email TEXT, password TEXT)")
function adduser(username, email, password){
    db.run("INSERT INTO people (username, email, password) VALUES (?, ?, ?) [usernameset, emailset, passwordset]")
    window.location.href = thankyou.html

}

db.all("Sellect")


