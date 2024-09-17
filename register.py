from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
from login import *


class Register_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        # ================variables======================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contectNo = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_fname = StringVar()
        self.var_passw = StringVar()
        self.var_conpassw = StringVar()

        img1bg = Image.open(r"project_Images\background.PNG")
        img1bg = img1bg.resize((1570, 790), Image.ANTIALIAS)
        self.photoImg1bg = ImageTk.PhotoImage(img1bg)
        bg_lbl = Label(self.root, image=self.photoImg1bg)
        bg_lbl.place(x=0, y=0, width=1530, height=790)

        # frame+=======================
        frame = Frame(self.root, bg="white")
        frame.place(x=10, y=52, width=820, height=510)
        get_str = Label(frame, text="REGISTER HERE", font=("times new roman", 17, "bold"), fg="red", bg="white")
        get_str.place(x=10, y=5)

        # label======================
        fname_label = Label(frame, text="First Name:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname_label.place(x=20, y=50)

        self.fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname.place(x=180, y=50)

        lname_label = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname_label.place(x=410, y=50)

        self.lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.lname.place(x=600, y=50)

        cn_label = Label(frame, text="Contact No:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        cn_label.place(x=20, y=100)

        self.cn = ttk.Entry(frame, textvariable=self.var_contectNo, font=("times new roman", 15, "bold"))
        self.cn.place(x=180, y=100)

        email_label = Label(frame, text="Email:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email_label.place(x=410, y=100)

        self.email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.email.place(x=600, y=100)

        seq_label = Label(frame, text="Sequrity question:", font=("times new roman", 15, "bold"), fg="black",
                          bg="white")
        seq_label.place(x=10, y=150)

        self.comboSeq = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 13, "bold"),
                                     state="readonly")
        self.comboSeq["values"] = ("select", "Your birth place name", "Your first school name", "Your first school day")
        self.comboSeq.place(x=180, y=150, width=205, height=30)
        self.comboSeq.current(0)

        seqAn_label = Label(frame, text="Sequrity Answer:", font=("times new roman", 15, "bold"), fg="black",
                            bg="white")
        seqAn_label.place(x=410, y=150)

        self.seqAn = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.seqAn.place(x=600, y=150)

        passw_label = Label(frame, text="Password:", font=("times new roman", 15, "bold"), fg="black", bg="white")
        passw_label.place(x=20, y=200)

        self.passw = ttk.Entry(frame, textvariable=self.var_passw, font=("times new roman", 15, "bold"))
        self.passw.place(x=180, y=200)

        conpass_label = Label(frame, text="Confirm Password:", font=("times new roman", 15, "bold"), fg="black",
                              bg="white")
        conpass_label.place(x=410, y=200)

        self.conpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.var_conpassw)
        self.conpass.place(x=600, y=200)

        # ===========checkBox===================
        self.var_chech = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_chech, onvalue=1, offvalue=0,
                               text="I Agree The Term And Condition", font=("times new roman", 15, "bold"), bg="white",
                               activebackground="white")
        checkbtn.place(x=20, y=250)
        # ========button===========

        login_label = Label(frame, text="if you are already register then click below to login",
                            font=("times new roman", 15, "bold"), fg="black",
                            bg="white")
        login_label.place(x=10, y=360)

        loginBtn = Button(frame, text="Login", font=("times new roman", 16, "bold"), bd=3,
                          relief=RIDGE, command=self.login_data,fg="white", bg="red", activebackground="red", activeforeground="white")
        loginBtn.place(x=10, y=400, width=225, height=35)

        # register button=================
        registerBtn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"),
                             relief=RIDGE, fg="white",
                             bg="red", activebackground="red", bd=3)
        registerBtn.place(x=10, y=310, width=225, height=35)

    # function===========================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_securityQ.get() == "select" or self.var_securityA.get() == "" or self.var_passw.get() == "":
            messagebox.showerror("Eroor", "All field require to fill")
        elif self.var_passw.get() != self.var_conpassw.get():
            messagebox.showerror("Eroor", "Confirm password and Password must be same")
        elif self.var_chech.get() == 0:
            messagebox.showerror("Eroor", "Please agree term and condition")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
            mycursor = conn.cursor()
            sql = "select * from register where email=%s"
            val = (self.var_email.get(),)
            mycursor.execute(sql, val)
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror("Eroor", "User already Exist,Please try another email")
                return
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contectNo.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_passw.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succes", "Register Successfully")

    def login_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_window(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Register_window(root)
    root.mainloop()
