import sqlite3

class SubjecFun:
    def __init__(self, data=[]):
    # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('Attandans.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS subject (id INTEGER PRIMARY KEY, Subject_name TEXT,ui text)''')
        self.conn.commit()
    
     
    def addSubject(self,Subject_name):
      self.cursor.execute('''INSERT INTO subject (Subject_name ,ui) VALUES (?,?)''',(Subject_name,'emty')  )
      self.conn.commit()
  
    def listSubject(self):
      stdReselt = self.cursor.execute("SELECT Subject_name FROM subject")
      return stdReselt

    
    def listSubjectName(self):
      stdReselt = self.cursor.execute("SELECT Subject_name FROM subject")
      self.conn.commit()
      return stdReselt

    def count_all_rows(self):
        with sqlite3.connect('Attandans.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM subject")
            result = cursor.fetchone()
            res = f"Total subject \n\n {result[0]}"
            return res
