# Importing required libraries
import csv
import sqlite3

# Creating a sqlite3 database and connecting to it
con = sqlite3.connect("data.db")
cur = con.cursor()

# Creating tables in the db as per the given csv file
cur.execute("CREATE TABLE t (id, first_name, last_name, email, gender, ip_address);")

# Opening the csv file for writing it's data to the database
with open('DATA.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['first_name'], i['last_name'], i['email'], i['gender'], i['ip_address']) for i in dr]

cur.executemany("INSERT INTO t (id, first_name, last_name, email, gender, ip_address) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()

#Verifying that the data is safely loaded to the database
for row in cur.execute('SELECT * FROM t LIMIT 10'):
    print(row)

# Closing the sqlite db connection
con.close()

