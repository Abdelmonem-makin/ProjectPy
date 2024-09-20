import cv2
import numpy as np
import face_recognition as face_rec
import os
from datetime import datetime
import tkinter as tk
from tkinter import Button
import sqlite3
import threading
import queue

def resize(img, size):
    width = int(img.shape[1] * size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

def get_students_from_db():
    with sqlite3.connect('Attandans.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, img, rollNum FROM studant")
        students = cursor.fetchall()
    return students

students = get_students_from_db()

studentImg = []
studentName = []
roll_Number = []
images_folder = 'Std_images'
for student in students:
    name, image_name, rollNum = student
    image_path = os.path.join(images_folder, image_name)
    if os.path.exists(image_path):
        curimg = cv2.imread(image_path)
        studentImg.append(curimg)
        studentName.append(name)
        roll_Number.append(rollNum)
    else:
        print(f"Not Found: {image_name}")

def findEncoding(images):
    imgEncodings = []
    for img in images:
        img = resize(img, 0.50)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encodeimg = face_rec.face_encodings(img)[0]
            imgEncodings.append(encodeimg)
        except IndexError:
            print("No face found in the image.")
    return imgEncodings

def db_thread_func(q, Subject):
    while True:
        name, rollNumber = q.get()
        if name is None:
            break
        with sqlite3.connect('Attandans.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT count_attend FROM Attendance WHERE rollNum = ? AND Subject_name = ?", (rollNumber, Subject))
            result = cursor.fetchone()
            if result is None:
                now = datetime.now()
                data = now.strftime('%d-%m-%Y')
                cursor.execute(
                    'INSERT INTO Attendance (Std_name, Subject_name, Admin, Day, RollNum, count_attend) VALUES (?,?,?,?,?,?)',
                    (name, Subject, 'Admin', data, rollNumber, 1))
            else:
                cursor.execute("UPDATE Attendance SET count_attend = count_attend + 1 WHERE rollNum = ? AND Subject_name = ?",
                               (rollNumber, Subject))
            conn.commit()

def Attendance(vid, studentImg, studentName, roll_Number, findEncoding, q):
    EncodeList = findEncoding(studentImg)
    global running
    running = True

    while running:
        success, frame = vid.read()
        Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        facesInFrame = face_rec.face_locations(Smaller_frames)
        encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

        for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
            matches = face_rec.compare_faces(EncodeList, encodeFace)
            facedis = face_rec.face_distance(EncodeList, encodeFace)
            matchIndex = np.argmin(facedis)

            if matches[matchIndex]:
                name = studentName[matchIndex].upper()
                rollNum = roll_Number[matchIndex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                q.put((name, rollNum))

        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

# Initialize video capture
vid = cv2.VideoCapture(0)

# Create a queue and start the database thread
q = queue.Queue()
subject = "OOP"  # Replace with the actual subject name
db_thread = threading.Thread(target=db_thread_func, args=(q, subject))
db_thread.start()

# Start the attendance function
Attendance(vid, studentImg, studentName, roll_Number, findEncoding, q)

# Stop the database thread
q.put((None, None))
db_thread.join()
