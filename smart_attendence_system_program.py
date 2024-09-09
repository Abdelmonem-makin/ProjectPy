import os
from datetime import datetime
import customtkinter as ctk
import cv2
import face_recognition as face_rec
import numpy as np

ctk.set_appearance_mode("System")


def MarkAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myFatalist = f.readlines()
        nameList = []
        for line in myFatalist:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            timestr = now.strftime('%H:%M')
            f.writelines(f'\n{name}, {timestr}')

def resize(img, size):
    width = int(img.shape[1] * size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

class attendance(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Attendance Using Face Recognition")
        self.geometry("500x500")
        path = 'Std_images'
        studantImg = []
        studantName = []
        myList = os.listdir(path)
        for img in myList:
            curlimg = cv2.imread(f'{path}/{img}')
            studantImg.append(curlimg)
            studantName.append(os.path.splitext(img)[0])
        # print('{}'.format(studantName))
        print(studantName)

        EncodeList = self.findEncoding(studantImg)
        vid = cv2.VideoCapture(0)
        while True:
            success, frame = vid.read()
            Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            facesInFrame = face_rec.face_locations(Smaller_frames)
            encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

            for encodeFace, facelet in zip(encodeFacesInFrame, facesInFrame):
                matches = face_rec.compare_faces(EncodeList, encodeFace)
                facedis = face_rec.face_distance(EncodeList, encodeFace)
                print(facedis)
                matchIndex = np.argmin(facedis)

                if matches[matchIndex]:
                    name = studantName[matchIndex].upper()
                    y1, x2, y2, x1 = facelet
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    MarkAttendance(name)

            cv2.imshow('video', frame)
            cv2.waitKey(1)

    def findEncoding(self ,images):
        imgEncodings = []
        for img in images:
            img = resize(img, 0.50)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodeimg = face_rec.face_encodings(img)[0]
            imgEncodings.append(encodeimg)
        return imgEncodings


app = attendance()
app.mainloop()
