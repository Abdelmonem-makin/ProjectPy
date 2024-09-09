import sqlite3

class AttendanceFun:
    def __init__(self, data=[]):
    # Connect to the database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('Attandans.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Attendance (id INTEGER PRIMARY KEY,Std_name TEXT NOT NULL,
        Subject_name text,Admin TEXT,Day TEXT,RollNum TEXT ,UNIQUE (rollNum, Day))''')
        self.conn.commit()
    
    def addAttendance(self,Std_name, Subject_name ,Admin,Day,rollNumber):
      self.cursor.execute('''INSERT INTO Attendance (Std_name, Subject_name, Admin, Day, RollNum) VALUES (?,?,?,?,?)''',(Std_name, Subject_name, Admin, Day, rollNumber))
      self.conn.commit()

    def updataStudant(self,name,img,rollNum,Stdsearch):
      self.cursor.execute("UPDATE studant SET name='"+name+"', img='"+img+"' ,rollNum='"+rollNum+"' WHERE rollNum='"+Stdsearch+"'") 
      self.conn.commit()
     
    def listAttendance(self):
      stdReselt = self.cursor.execute("SELECT rollNum,Std_name, Subject_name ,Admin,Day FROM Attendance")
      return stdReselt