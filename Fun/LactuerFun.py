import sqlite3
import datetime


class lacTableFun:
    def __init__(self, data=[]):
        # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('Attandans.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Lac_table (id INTEGER PRIMARY KEY,day TEXT,subj_name TEXT 
        NOT NULL,Date text,Teacher text)''')
        self.conn.commit()

    def addLacTable(self, subj_name, Date, day, Teacher):
        self.cursor.execute('''INSERT INTO Lac_table (subj_name, Date ,day,Teacher) VALUES (?,?,?,?)''',
                            (subj_name, Date, day, Teacher))
        self.conn.commit()

    def listLacTable(self):
        Reselt = self.cursor.execute("SELECT Date,day,subj_name,Teacher  FROM Lac_table")
        self.conn.commit()
        return Reselt

    def toDayLac(self):
        self.now = datetime.datetime.now()
        self.timeStar = self.now.strftime("%w")
        if int(self.timeStar) == 1:
            self.timeStar = "Mon"
        elif int(self.timeStar) == 2:
            self.timeStar = "Tue"
        elif int(self.timeStar) == 3:
            self.timeStar = "Wed"
        elif int(self.timeStar) == 4:
            self.timeStar = "Thu"
        elif int(self.timeStar) == 5:
            self.timeStar = "Sat"
        else:
            self.timeStar = "Sun"

        Resell = self.cursor.execute(
            "SELECT Date,day,subj_name,Teacher FROM Lac_table WHERE Date='" + self.timeStar + "'")
        self.conn.commit()
        return Resell

    def list_Atten_Subject(self):
        self.now = datetime.datetime.now()
        self.timeStar = self.now.strftime("%w")
        if int(self.timeStar) == 1:
            self.timeStar = "Mon"
        elif int(self.timeStar) == 2:
            self.timeStar = "Tue"
        elif int(self.timeStar) == 3:
            self.timeStar = "Wed"
        elif int(self.timeStar) == 4:
            self.timeStar = "Thu"
        elif int(self.timeStar) == 5:
            self.timeStar = "Sat"
        else:
            self.timeStar = "Sun"

        Reselt = self.cursor.execute(
            "SELECT subj_name FROM Lac_table WHERE Date='" + self.timeStar + "'")
        self.conn.commit()
        return Reselt
