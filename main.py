import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from attendance import Attendance
import os
from time import  strftime
from datetime import datetime
from train import Train
from face_Recognizer import FaceRecognizer
from help import Help



class Face_Recogination_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # firstImage
        img1 = Image.open(r"project_Images\aktuImg.jpg")
        img1 = img1.resize((520, 130), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoImg1)
        f_lbl1.place(x=0, y=-40, width=515, height=190)

        img2 = Image.open(r"project_Images\facerecoginition.PNG")
        img2 = img2.resize((520, 130), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoImg)
        f_lbl2.place(x=515, y=-80, width=515, height=280)

        img3 = Image.open(r"project_Images\bansal.jpg")
        img3 = img3.resize((520, 130), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoImg3)
        f_lbl3.place(x=1025, y=-40, width=515, height=190)

        img1bg = Image.open(r"project_Images\background.PNG")
        img1bg = img1bg.resize((1570, 730), Image.ANTIALIAS)
        self.photoImg1bg = ImageTk.PhotoImage(img1bg)
        bg_lbl = Label(self.root, image=self.photoImg1bg)
        bg_lbl.place(x=0, y=120, width=1550, height=730)

        title_lbl = Label(bg_lbl, text="SMART ATTENDENCE SYSTEM", font=("times new roman", 25, "bold"),
                          bg="red", fg="YELLOW")
        title_lbl.place(x=-3, y=-1, width=1550, height=35)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman", 25, "bold"),background='red',foreground='blue')
        lbl.place(x=5,y=0,width=210,height=35)
        time()

        # Student button
        img4 = Image.open(r"project_Images\student.jpg")
        img4 = img4.resize((190, 190), Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_lbl, image=self.photoImg4, command=self.student_detail, cursor="hand2")
        b1.place(x=0, y=35, width=190, height=190)

        b1_1 = Button(bg_lbl, text="STUDENT DETAIL", cursor="hand2", command=self.student_detail, borderwidth=3,
                      font=("times new roman", 15, "bold"), bg="yellow", fg="black")
        b1_1.place(x=0, y=220, width=190, height=30)

        # face detector
        img5 = Image.open(r"project_Images\facedetect.jpg")
        img5 = img5.resize((190, 190), Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_lbl, image=self.photoImg5, cursor="hand2",command=self.face_data)
        b2.place(x=220, y=35, width=190, height=190)

        b2_2 = Button(bg_lbl, text="FACE DETECT", cursor="hand2",command=self.face_data, borderwidth=3, font=("times new roman", 15, "bold"),
                      bg="yellow", fg="black")
        b2_2.place(x=220, y=220, width=190, height=30)

        # attendence view
        img6 = Image.open(r"project_Images\attendence.jpg")
        img6 = img6.resize((190, 190), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_lbl, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=440, y=35, width=190, height=190)

        b3_3 = Button(bg_lbl, text="ATTENDENCE", cursor="hand2",command=self.attendance_data,borderwidth=3, font=("times new roman", 15, "bold"),
                      bg="yellow", fg="black")
        b3_3.place(x=440, y=220, width=190, height=30)

        # Train data
        img8 = Image.open(r"project_Images\trainData.png")
        img8 = img8.resize((190, 190), Image.ANTIALIAS)
        self.photoImg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_lbl, command=self.train_data, image=self.photoImg8, cursor="hand2")
        b4.place(x=660, y=35, width=190, height=190)

        b4_4 = Button(bg_lbl, text="TRAIN DATA", command=self.train_data, cursor="hand2", borderwidth=3,
                      font=("times new roman", 15, "bold"),
                      bg="yellow", fg="black")
        b4_4.place(x=660, y=220, width=190, height=30)

        # photo
        img9 = Image.open(r"project_Images\photo.jpg")
        img9 = img9.resize((200, 220), Image.ANTIALIAS)
        self.photoImg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_lbl, image=self.photoImg9, command=self.open_Img, cursor="hand2")
        b5.place(x=0, y=300, width=190, height=190)

        b5_5 = Button(bg_lbl, text="PHOTO", command=self.open_Img, cursor="hand2", borderwidth=3,
                      font=("times new roman", 15, "bold"),
                      bg="yellow", fg="black")
        b5_5.place(x=0, y=490, width=190, height=30)
        # help porta
        img7 = Image.open(r"project_Images\helpMe.png")
        img7 = img7.resize((190, 190), Image.ANTIALIAS)
        self.photoImg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bg_lbl, image=self.photoImg7, cursor="hand2",command=self.help_data)
        b6.place(x=220, y=300, width=190, height=190)

        b6_6 = Button(bg_lbl, text="HELP", cursor="hand2", borderwidth=3, font=("times new roman", 15, "bold"),
                      bg="yellow", fg="black",command=self.help_data)
        b6_6.place(x=220, y=490, width=190, height=30)

        # EXIT
        img10 = Image.open(r"project_Images\exit.jpg")
        img10 = img10.resize((210, 215), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_lbl, image=self.photoimg10, cursor="hand2",command=self.iExit)
        b7.place(x=440, y=300, width=190, height=190)

        b7_7 = Button(bg_lbl, text="EXIT", cursor="hand2", borderwidth=3, font=("times new roman", 15, "bold"),
                      bg="yellow", fg="black",command=self.iExit)
        b7_7.place(x=440, y=490, width=190, height=30)

    def open_Img(self):
        os.startfile("data")

    # ===================================================================================

    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognizer(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recogination_System(root)
    root.mainloop()
