import sqlite3

db = sqlite3.connect("contacts.sqlite")     # creating contacts sqlite database

name = input("Please enter a name to search for: ")

for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(row)

db.close()
