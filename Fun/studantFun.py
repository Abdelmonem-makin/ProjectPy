import sqlite3


class studantFun:
    def __init__(self, data=[]):
        # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('Attandans.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS studant (id INTEGER PRIMARY KEY,name TEXT NOT NULL,img text,rollNum text)''')
        self.conn.commit()

    def addStudant(self, name, img, rollNum):
        self.cursor.execute('''INSERT INTO studant (name, img ,rollNum) VALUES (?,?,?)''', (name, img, rollNum))
        self.conn.commit()

    def updataStudant(self, name, img, rollNum, Stdsearch):
        self.cursor.execute(
            "UPDATE studant SET name='" + name + "', img='" + img + "' ,rollNum='" + rollNum + "' WHERE rollNum='" + Stdsearch + "'")
        self.conn.commit()

    def listStudant(self):
        stdReselt = self.cursor.execute("SELECT rollNum,name ,img FROM studant")
        return stdReselt

    def get_studant(self):
        with sqlite3.connect('Attandans.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, img, rollNum FROM studant")
            students = cursor.fetchall()
        return students

    def count_all_rows(self):
        with sqlite3.connect('Attandans.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM studant")
            result = cursor.fetchone()
            res = f"Total studant \n\n {result[0]}"
            return res
