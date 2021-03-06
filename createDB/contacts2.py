import sqlite3

db = sqlite3.connect("contacts.sqlite")     # creating contacts sqlite database

new_email = "newemail@update.com"
phone = input("Please Enter The Phone Number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))     # executescript() runs more than one SQL statement in one call
print("{} rows updated".format(update_cursor.rowcount))

print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-"*20)

db.close()
