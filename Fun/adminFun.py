import sqlite3

class adminFun:
    def __init__(self, data=[]):
    # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('Attandans.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY,userName TEXT NOT NULL,type text,password text)''')
        self.conn.commit()
    
    def addAdmin(self,userName,type,password):
      self.cursor.execute('''INSERT INTO admin (userName, type ,password) VALUES (?,?,?)''',(userName,type,password))
      self.conn.commit()
    #   return "Add success"
  
    def listAdmin(self):
      stdReselt = self.cursor.execute("SELECT userName ,type FROM admin")
      return stdReselt