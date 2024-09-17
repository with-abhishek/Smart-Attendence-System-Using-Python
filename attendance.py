from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #================variables=======
        self.var_attend_Id=StringVar()
        self.var_attend_roll= StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

        # firstImage
        img1 = Image.open(r"project_Images\student4.jpg")
        img1 = img1.resize((885, 220), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoImg1)
        f_lbl1.place(x=0, y=-40, width=880, height=220)
        # second image
        img2 = Image.open(r"project_Images\student1.jpg")
        img2 = img2.resize((860, 220), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoImg)
        f_lbl2.place(x=765, y=-80, width=850, height=300)

        img1bg = Image.open(r"project_Images\background.PNG")
        img1bg = img1bg.resize((1530, 730), Image.ANTIALIAS)
        self.photoImg1bg = ImageTk.PhotoImage(img1bg)
        bg_lbl = Label(self.root, image=self.photoImg1bg)
        bg_lbl.place(x=0, y=120, width=1530, height=730)

        title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"),
                          bg="red", fg="black")
        title_lbl.place(x=-3, y=-1, width=1530, height=45)

        # main frame
        mainFrame = Frame(bg_lbl, bd=2, bg="white")
        mainFrame.place(x=10, y=48, width=1505, height=610)

        # left level frame
        leftFrame = LabelFrame(mainFrame, bd=2, bg="white", text="Student Attendance Detail",
                               font=("times new roma", 12, "bold"))
        leftFrame.place(x=5, y=7, width=660, height=520)

        img_left = Image.open(r"project_Images\student1.jpg")
        img_left = img_left.resize((660, 100), Image.ANTIALIAS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(leftFrame, image=self.photoImg_left)
        f_lbl_left.place(x=0, y=0, width=655, height=100)

        leftInsideFrame = Frame(leftFrame, bd=2, relief=RIDGE, bg="white")
        leftInsideFrame.place(x=0, y=103, width=650, height=390)

        # Labels and entry
        # attendance entry

        attendance_id_lebel = Label(leftInsideFrame, text="Attendance Id:", bg="white",
                                    font=("times new roman", 13, "bold"))
        attendance_id_lebel.grid(row=0, column=0, padx=5, sticky=W)

        attendance_id_Entry = ttk.Entry(leftInsideFrame, width=20,textvariable=self.var_attend_Id,
                                        font=("times new roman", 11, "bold"))
        attendance_id_Entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # roll Label

        rolllebel = Label(leftInsideFrame, text="Roll No:", bg="white",
                          font=("times new roman", 13, "bold"))
        rolllebel.grid(row=0, column=2, padx=5, sticky=W)

        rolllebel_Entry = ttk.Entry(leftInsideFrame, width=20,textvariable=self.var_attend_roll,
                                    font=("times new roman", 11, "bold"))
        rolllebel_Entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # name

        namelebel = Label(leftInsideFrame, text="Name:", bg="white",
                          font=("times new roman", 13, "bold"))
        namelebel.grid(row=1, column=0, padx=5, sticky=W)

        namelebel_Entry = ttk.Entry(leftInsideFrame, width=20,textvariable=self.var_attend_name,
                                    font=("times new roman", 11, "bold"))
        namelebel_Entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # department

        departmentlebel = Label(leftInsideFrame, text="Depaartment:", bg="white",
                                font=("times new roman", 13, "bold"))
        departmentlebel.grid(row=1, column=2, padx=5, sticky=W)

        departmentlebel_Entry = ttk.Entry(leftInsideFrame, width=20,textvariable=self.var_attend_dep,font=("times new roman", 11, "bold"))
        departmentlebel_Entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # time

        timelebel = Label(leftInsideFrame, text="Time:", bg="white",
                          font=("times new roman", 13, "bold"))
        timelebel.grid(row=2, column=0, padx=5, sticky=W)

        timelebel_Entry = ttk.Entry(leftInsideFrame, width=20,textvariable=self.var_attend_time,
                                    font=("times new roman", 11, "bold"))
        timelebel_Entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # date

        datelebel = Label(leftInsideFrame, text="Date:", bg="white",
                          font=("times new roman", 13, "bold"))
        datelebel.grid(row=2, column=2, padx=5, sticky=W)

        datelebel_Entry = ttk.Entry(leftInsideFrame, width=20,textvariable=self.var_attend_date,
                                    font=("==times new roman", 11, "bold"))
        datelebel_Entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Attendance

        Attendancelebel = Label(leftInsideFrame, text="Attendance Status:", bg="white",
                                font=("times new roman", 13, "bold"))
        Attendancelebel.grid(row=3, column=0, padx=5, sticky=W)

        self.atten_status = ttk.Combobox(leftInsideFrame, width=20,textvariable=self.var_attend_attendance, font=("times new roman", 11, "bold"),
                                         state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=5, sticky=W)
        self.atten_status.current(0)

        # button frame
        btn1_Frame = LabelFrame(leftInsideFrame, bd=2, bg="white", relief=RIDGE)
        btn1_Frame.place(x=0, y=300, width=647, height=45)

        # Import Button
        ImportBtn = Button(btn1_Frame, text="Import Csv", command=self.importCsv, width=16, height=1,
                           font=("times new roman", 17, "bold"), bg="blue", fg="white")
        ImportBtn.grid(row=0, column=0)
        # Export buttton
        exportBtn = Button(btn1_Frame, text="Export Csv", width=16, command=self.exportCsv,
                           font=("times new roman", 17, "bold"), bg="blue", fg="white")
        exportBtn.grid(row=0, column=1)
        # # Update button
        # updateBtn = Button(btn1_Frame, text="Update", width=15,
        #                    font=("times new roman", 13, "bold"), bg="blue", fg="white")
        # updateBtn.grid(row=0, column=2)
        # reset buttton
        resetBtn = Button(btn1_Frame, text="Reset", width=15,
                          font=("times new roman", 16, "bold"), bg="blue",
                          fg="white",command=self.resetdata)
        resetBtn.grid(row=0, column=2)

        # right level frame
        rightFrame = LabelFrame(mainFrame, bd=2, bg="white", text="Attendance Detail",
                                font=("times new roma", 12, "bold"))
        rightFrame.place(x=670, y=7, width=655, height=520)

        table_Frame = LabelFrame(rightFrame, bd=2, bg="white", relief=RIDGE)
        table_Frame.place(x=3, y=3, width=645, height=485)

        # ================Scroll bar=========================
        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_Frame, columns=(
        "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=140)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ======================fetch data=================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Csv",
                                         filetypes=(("CSV File", "*.csv"), ("All iles", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", " No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open Csv",
                                               filetypes=(("CSV File", "*.csv"), ("All iles", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data is exported to " + os.path.basename(fln) + "succesfully")
        except EXCEPTION as es:
            messagebox.showerror("Eroor", f" Due to :{str(es)}", parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_attend_Id.set(row[0])
        self.var_attend_roll.set(row[1])
        self.var_attend_name.set(row[2])
        self.var_attend_dep.set(row[3])
        self.var_attend_time.set(row[4])
        self.var_attend_date.set(row[5])
        self.var_attend_attendance.set(row[6])


    def resetdata(self):
        self.var_attend_Id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
