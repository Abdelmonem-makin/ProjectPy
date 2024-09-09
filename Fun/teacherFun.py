import sqlite3

class teacherFun:
    def __init__(self, data=[]):
    # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('Attandans.db')
        self.conn.row_factory = sqlite3.Row
        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teacher (id INTEGER PRIMARY KEY,name TEXT NOT NULL,subj_ID INTEGER,Phone_num INTEGER)''')
        self.conn.commit()

    def addTeacher(self,name,subj_ID,Phone_num):
        self.cursor.execute('''INSERT INTO teacher (name, subj_ID ,Phone_num) VALUES (?,?,?)''',(name,subj_ID,Phone_num))
        self.conn.commit()
  
    def lisTeacher(self):
      stdReselt = self.cursor.execute("SELECT name ,subj_ID,Phone_num FROM teacher")
      return stdReselt
  
    
    def lisTeacherName(self):
      stdReselt = self.cursor.execute("SELECT name FROM teacher")
      self.conn.commit()
      return stdReselt