from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class FaceRecognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognization", font=("times new roman", 25, "bold"), bg="white",
                          fg="black")
        title_lbl.place(x=-3, y=-1, width=1430, height=45)

        img_top = Image.open(r"project_Images\facedetect1.jpg")
        img_top = img_top.resize((750, 650), Image.ANTIALIAS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)
        f_lbl_left = Label(self.root, image=self.photoImg_top)
        f_lbl_left.place(x=0, y=45, width=730, height=650)

        img_bottom = Image.open(r"project_Images\facedetectPhone.png")
        img_bottom = img_bottom.resize((730, 660), Image.ANTIALIAS)
        self.photoImg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_right = Label(self.root, image=self.photoImg_bottom)
        f_lbl_right.place(x=730, y=45, width=730, height=650)

        b1_1 = Button(f_lbl_right, text="FACE RECOGNITION",command=self.face_recog,cursor="hand2", borderwidth=3,
                      font=("times new roman", 20, "bold"), bg="red", fg="white")
        b1_1.place(x=192, y=512, width=328, height=65)

        #============================attendence==========

    def mark_attendence(self,id,r,n,d):
        with open("badru.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if (id not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{r},{n},{d},{dtstring},{d1},present")




        # ========face recognition==================

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
                mycursor = conn.cursor()

                mycursor.execute("select Name from student where StudentId=" + str(id))
                n = mycursor.fetchone()
                n = "+".join(n)

                mycursor.execute("select Roll from student where StudentId=" + str(id))
                r = mycursor.fetchone()
                r = "+".join(r)

                mycursor.execute("select Dep from student where StudentId=" + str(id))
                d = mycursor.fetchone()
                d = "+".join(d)

                mycursor.execute("select StudentId from student where StudentId=" + str(id))
                id = mycursor.fetchone()
                id = "+".join(id)

                if confidence > 77:
                    cv2.putText(img, f"ID: {id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                    self.mark_attendence(id,r,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xls")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognizer(root)
    root.mainloop()
