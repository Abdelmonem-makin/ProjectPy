# import cv2
# import numpy as np
# import face_recognition as face_rec
# import os
# from datetime import datetime
# import tkinter as tk
# from tkinter import Button, Label
# from PIL import Image, ImageTk
# import sqlite3

# def resize(img, size):
#     width = int(img.shape[1] * size)
#     height = int(img.shape[0] * size)
#     dimension = (width, height)
#     return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

# def enhance_image(image):
#     # تحويل الصورة إلى تدرجات الرمادي
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     # تطبيق مرشح إزالة الضوضاء
#     denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)
    
#     # زيادة التباين باستخدام CLAHE
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     enhanced = clahe.apply(denoised)
    
#     return enhanced

# # الاتصال بقاعدة البيانات واسترجاع بيانات الطلاب
# conn = sqlite3.connect('Attandans.db')
# cursor = conn.cursor()
# cursor.execute("SELECT name, img FROM studant")
# students = cursor.fetchall()
# cursor.close()
# conn.close()

# studentImg = []
# studentName = []
# for student in students:
#     name, img = student
#     curimg = cv2.imread(img)
#     print(student)
#     # curimg = enhance_image(curimg)  # تحسين الصورة
#     studentImg.append(curimg)
#     studentName.append(name)

# def findEncoding(images):
#     imgEncodings = []
#     for img in images:
#         img = resize(img, 0.50)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encodeimg = face_rec.face_encodings(img)[0]
#         imgEncodings.append(encodeimg)
#     return imgEncodings

# def MarkAttendence(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDatalist = f.readlines()
#         nameList = [line.split(',')[0] for line in myDatalist]
#         if name not in nameList:
#             now = datetime.now()
#             timestr = now.strftime('%H:%M')
#             f.writelines(f'\n{name}, {timestr}')

# def close_video():
#     global running
#     running = False
#     root.quit()  # إغلاق نافذة tkinter

# def Attendance(vid, studentImg, studentName, findEncoding, MarkAttendence, label):
#     EncodeList = findEncoding(studentImg)
#     global running
#     running = True

#     while running:
#         success, frame = vid.read()
#         if not success:
#             break

#         Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
#         facesInFrame = face_rec.face_locations(Smaller_frames)
#         encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

#         for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
#             matches = face_rec.compare_faces(EncodeList, encodeFace)
#             facedis = face_rec.face_distance(EncodeList, encodeFace)
#             matchIndex = np.argmin(facedis)

#             if matches[matchIndex]:
#                 name = studentName[matchIndex].upper()
#                 y1, x2, y2, x1 = faceloc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
#                 cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 255, 0), cv2.FILLED)
#                 cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 MarkAttendence(name)

#         # تحويل إطار الفيديو إلى صورة يمكن عرضها في tkinter
#         img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(img)
#         imgtk = ImageTk.PhotoImage(image=img)
#         label.imgtk = imgtk
#         label.configure(image=imgtk)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     vid.release()
#     cv2.destroyAllWindows()

# root = tk.Tk()
# root.title("Face Recognition Attendance System")

# # إنشاء إطار لعرض الفيديو
# label = Label(root)
# label.pack()

# # إضافة زر الإغلاق
# close_button = Button(root, text="Close", command=close_video)
# close_button.pack()

# vid = cv2.VideoCapture(0)

# # تشغيل الفيديو في نافذة tkinter
# import threading
# video_thread = threading.Thread(target=Attendance, args=(vid, studentImg, studentName, findEncoding, MarkAttendence, label))
# video_thread.start()

# root.mainloop()

# # تأكد من إغلاق الكاميرا بعد إغلاق نافذة tkinter
# running = False
# vid.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
import face_recognition as face_rec
import os
from datetime import datetime
import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import sqlite3

def resize(img, size):
    width = int(img.shape[1] * size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

# الاتصال بقاعدة البيانات واسترجاع بيانات الطلاب
conn = sqlite3.connect('Attandans.db')
cursor = conn.cursor()
cursor.execute("SELECT name, img FROM studant")
students = cursor.fetchall()
cursor.close()
conn.close()

studentImg = []
studentName = []
images_folder = 'Std_images'
for student in students:
    name, image_name = student
    image_path = os.path.join(images_folder, image_name)
    if os.path.exists(image_path):
        curimg = cv2.imread(image_path)
        studentImg.append(curimg)
        studentName.append(name)
    else:
        print(f"Not Found: {image_name}")

def findEncoding(images):
    imgEncodings = []
    for img in images:
        img = resize(img, 0.50)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeimg = face_rec.face_encodings(img)[0]
        imgEncodings.append(encodeimg)
    return imgEncodings

def MarkAttendence(name):
    with open('Attendance.csv', 'r+') as f:
        myDatalist = f.readlines()
        nameList = [line.split(',')[0] for line in myDatalist]
        if name not in nameList:
            now = datetime.now()
            timestr = now.strftime('%H:%M')
            f.writelines(f'\n{name}, {timestr}')

def close_video():
    global running
    running = False
    root.quit()  # إغلاق نافذة tkinter

def reduce_flicker(frame):
    return cv2.GaussianBlur(frame, (5, 5), 0)

def Attendance(vid, studentImg, studentName, findEncoding, MarkAttendence, label):
    EncodeList = findEncoding(studentImg)
    global running
    running = True

    while running:
        success, frame = vid.read()
        if not success:
            break

        frame = reduce_flicker(frame)  # تطبيق المرشح لتقليل الوميض

        Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        facesInFrame = face_rec.face_locations(Smaller_frames)
        encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

        for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
            matches = face_rec.compare_faces(EncodeList, encodeFace)
            facedis = face_rec.face_distance(EncodeList, encodeFace)
            matchIndex = np.argmin(facedis)

            if matches[matchIndex]:
                name = studentName[matchIndex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                MarkAttendence(name)

        # تحويل إطار الفيديو إلى صورة يمكن عرضها في tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Face Recognition Attendance System")

# إنشاء إطار لعرض الفيديو
label = Label(root)
label.pack()

# إضافة زر الإغلاق
close_button = Button(root, text="Close", command=close_video)
close_button.pack()

vid = cv2.VideoCapture(0)

# تشغيل الفيديو في نافذة tkinter
import threading
video_thread = threading.Thread(target=Attendance, args=(vid, studentImg, studentName, findEncoding, MarkAttendence, label))
video_thread.start()

root.mainloop()

# تأكد من إغلاق الكاميرا بعد إغلاق نافذة tkinter
running = False
vid.release()
cv2.destroyAllWindows()
