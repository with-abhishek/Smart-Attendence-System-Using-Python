from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 25, "bold"),
                          bg="red", fg="black")
        title_lbl.place(x=-3, y=-1, width=1430, height=35)

        img_top = Image.open(r"project_Images\background.PNG")
        img_top = img_top.resize((1430, 720), Image.ANTIALIAS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = Label(self.root, image=self.photoImg_top)
        f_lbl_left.place(x=0, y=35, width=1430, height=690)

        help_lbl=Label(f_lbl_left,text="Badrudozaansari0786@gmail.com", font=("times new roman", 25, "bold"), fg="black")
        help_lbl.place(x=450,y=300)

        help_lbl2 = Label(f_lbl_left, text="Ataulhaq@gmail.com", font=("times new roman", 25, "bold"),
                         fg="black")
        help_lbl2.place(x=450, y=350)

        help_lbl3 = Label(f_lbl_left, text="Ajayrajpoot@gmail.com", font=("times new roman", 25, "bold"),
                         fg="black")
        help_lbl3.place(x=450, y=400)

        help_lbl4= Label(f_lbl_left, text="Abhisheksing@gmail.com", font=("times new roman", 25, "bold"),
                         fg="black")
        help_lbl4.place(x=450, y=450)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()