import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd


def get_students_from_db():
    conn = sqlite3.connect('Attandans.db')  # Ensure this path is correct
    cursor = conn.cursor()

    cursor.execute("SELECT name, img, rollNum FROM studant")
    students = cursor.fetchall()

    conn.close()
    return students


def db_thread_func():
    conn = sqlite3.connect('Attandans.db')
    cursor = conn.cursor()

    roll_num = 'some_roll_num'
    day = 'some_day'

    cursor.execute("SELECT 1 FROM Attendance WHERE RollNum = ? AND Day = ?", (roll_num, day))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO Attendance (RollNum, Day, ...) VALUES (?, ?, ...)", (roll_num, day, ...))
        conn.commit()
    else:
        print("Entry already exists")

    conn.close()


def export_to_excel():
    # try:
        conn = sqlite3.connect('Attandans.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Attendance")
        data = cursor.fetchall()

        # Define column names based on your table structure
        columns = [desc[0] for desc in cursor.description]

        # Create a DataFrame and save it to an Excel file
        df = pd.DataFrame(data, columns=columns)
        df.to_excel('attendance.xlsx', index=False)

        conn.close()
        messagebox.showinfo("Success", "Attendance data exported to attendance.xlsx successfully!")
    # except Exception as e:
    #     messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("Attendance System")

# Create the export button
export_button = tk.Button(root, text="Export to Excel", command=export_to_excel)
export_button.pack(pady=20)

# Run the application
root.mainloop()
