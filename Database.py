import sqlite3
import json

connection = None

class Database:
    global connection
    connection = sqlite3.connect('Data.db', check_same_thread=False)

    def __init__(self):
        self.db = connection
        self.cursor = connection.cursor()
        self.database = ''

    def createTable(self):
        global connection
        c = connection.cursor()
        c.execute('''
           CREATE TABLE if not exists country_data(
               countries text, 
               years numeric,
               yearvalues numeric   
           )''')
        connection.commit()

        print("\nDatabase created successfully!")

    def insertData(self, country, year, values):
        global connection
        c = connection.cursor()
        for i in range(len(country)):
            c.execute("INSERT INTO country_data VALUES (?, ?, ?)", (country[i], year[i], values[i]))
            connection.commit()

    def retrieveJson(self, valueQuery):
        global connection
        c = connection.cursor()
        c.row_factory = lambda cursor, row: row[0]
        c.execute(
            "SELECT years FROM country_data WHERE countries = 'Australia' ORDER BY years")  # execute a simple SQL select query
        yearColumn = c.fetchall()  # get all the results from the above query
        c.execute(valueQuery)
        valueColumn = c.fetchall()
        connection.commit()
        dict = {yearColumn[i]: valueColumn[i] for i in range(len(yearColumn))}
        json_string = json.dumps(dict, indent=6)
        # print(json_string)
        return json_string
