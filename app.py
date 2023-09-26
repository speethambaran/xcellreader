from flask import Flask, jsonify, request
import sqlite3
import csv
import os
from dotenv import load_dotenv

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
connection.close()
load_dotenv()
FILENAME = os.getenv('MYFILENAME')
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/

@app.route('/', methods = ['GET'])
def home():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    query = "SELECT * FROM `vehicleinfo`"
    cur.execute(query)
    rows = cur.fetchall()
    connection.close()
    return jsonify({'data': rows})

@app.route('/upload', methods = ['GET'])
def insertdata():
    connection = sqlite3.connect('database.db')
# opening the CSV file
    with open('4172.csv', mode ='r')as file:

# reading the CSV file
        csvFile = csv.reader(file)
        columns = next(csvFile)
        query = 'insert into vehicleinfo({0}) values ({1})'
        query = query.format(','.join(columns), ','.join('?' * len(columns)))
        cur = connection.cursor()
        for lines in csvFile:
            cur.execute(query, lines)
        connection.commit()
        connection.close()
        data = "data uploaded successfully"
        return jsonify({'data': data})
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)