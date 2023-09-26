import sqlite3
import csv

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    
# opening the CSV file
with open('4172.csv', mode ='r')as file:

# reading the CSV file
    csvFile = csv.reader(file)
    columns = next(csvFile)
    query = 'insert into posts({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cur = connection.cursor()
    for lines in csvFile:
        cur.execute(query, lines)
    connection.commit()
    connection.close()