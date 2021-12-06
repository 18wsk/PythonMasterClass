import sqlite3

db = sqlite3.connect("contacts.sqlite")     # creating contacts sqlite database
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Will', 6134842390, '18wsk@queensu.ca')")
db.execute("INSERT INTO contacts VALUES('Brian', 69420, 'brian@email.com')")

cursor = db.cursor()
# A database cursor is an object that enables traversal over the rows of a result set.
# It allows you to process individual row returned by a query.

cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())    # when a cursor runs out of lines it goes to close no matter if called line after

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit() # must commit to save changes --> can be accessed now by other files
db.close()  # neccessary to close SQL connection

