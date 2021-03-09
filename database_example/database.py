import sqlite3
import os.path


class DB:
    def initDB(self):
        if not os.path.exists('sqldb.db'):
            connection = sqlite3.connect('sqldb.db')
            cursor = connection.cursor()
            cursor.execute(
                '''CREATE TABLE persons(name TEXT, forename TEXT)''')
            return 'Database created'
        else:
            return 'Database exists'

    def readDB(self):
        dbString = ""
        counter = 0

        if os.path.exists('sqldb.db'):
            connection = sqlite3.connect('sqldb.db')
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM persons''')
            rows = cursor.fetchall()
            
            for row in rows:
                counter += 1
                dbString += row[0] + ", " + row[1] + "\n"

            connection.close()

            return [dbString, str(counter)]

        else:
            return "Database does not exist"

        return dbString

    def writeDB(self, n, v):
        
        if os.path.exists('sqldb.db'):
            connection = sqlite3.connect('sqldb.db')
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO persons VALUES(?,?)''', (n, v))
            connection.commit()
            connection.close()

            return "Data saved: " + n + ", " + v
        
        else:
            return "Database does not exist"
