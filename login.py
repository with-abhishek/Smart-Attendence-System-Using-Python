from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Face_Recogination_System
from register import*
import pymysql


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1570x790+0+0")
        self.root.title("Login System")

        img1bg = Image.open(r"project_Images\background.PNG")
        img1bg = img1bg.resize((1570, 790), Image.ANTIALIAS)
        self.photoImg1bg = ImageTk.PhotoImage(img1bg)
        bg_lbl = Label(self.root, image=self.photoImg1bg)
        bg_lbl.place(x=0, y=0, width=1530, height=790)

        frame = Frame(self.root, bg="white")
        frame.place(x=100, y=45, width=420, height=520)

        img2bg = Image.open(r"project_Images\iconLogin.jpg")
        img2bg = img2bg.resize((120, 130), Image.ANTIALIAS)
        self.photoImg2bg = ImageTk.PhotoImage(img2bg)
        bg_lbl1 = Label(self.root, image=self.photoImg2bg)
        bg_lbl1.place(x=260, y=44, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=140, y=102)

        # label======================
        username_label = Label(frame, text="User Name:", font=("times new roman", 16, "bold"), fg="black", bg="white")
        username_label.place(x=20, y=150)

        self.textuser = ttk.Entry(frame, font=("times new roman", 16, "bold"))
        self.textuser.place(x=140, y=150)
        # password===================

        password_label = Label(frame, text="Password:", font=("times new roman", 16, "bold"), fg="black", bg="white")
        password_label.place(x=20, y=200)

        self.textpassword = ttk.Entry(frame, font=("times new roman", 16, "bold"))
        self.textpassword.place(x=140, y=200)

        # login button=======================

        loginBtn = Button(frame, text="Login", font=("times new roman", 16, "bold"), command=self.log_in, bd=3,
                          relief=RIDGE, fg="black", bg="red", activebackground="red", activeforeground="black")
        loginBtn.place(x=142, y=250, width=125, height=35)

        # register button=================
        registerBtn = Button(frame, text="New User Register", command=self.register,
                             font=("times new roman", 15, "bold"), borderwidth=0,
                             relief=RIDGE, fg="black",
                             bg="white", activebackground="white", activeforeground="black")
        registerBtn.place(x=0, y=310, width=225, height=35)

        # forget button============
        forgetBtn = Button(frame, text="Forget your password", font=("times new roman", 15, "bold"), borderwidth=0,
                           relief=RIDGE, fg="black",
                           bg="white", activebackground="white", activeforeground="black")
        forgetBtn.place(x=10, y=350, width=225, height=35)

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_window(self.new_window)

    def log_in(self):
        if self.textuser.get() == "" or self.textpassword.get() == "":
            messagebox.showerror("Error", "Our field required")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s", (
                self.textuser.get(),
                self.textpassword.get(),

            ))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Eroor", "Invalid user name and password")
            else:
                open_main = messagebox.askyesno("YesNo", "Acces only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recogination_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_window(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Login_window(root)
    root.mainloop()
