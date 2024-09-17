from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========variables=======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year= StringVar()
        self.var_semester = StringVar()
        self.var_stdId= StringVar()
        self.var_stdName = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender= StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



# firstImage
        img1 = Image.open(r"project_Images\student3.jpg")
        img1 = img1.resize((520, 130), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoImg1)
        f_lbl1.place(x=0, y=-40, width=515, height=190)

        img2 = Image.open(r"project_Images\student1.jpg")
        img2 = img2.resize((520, 130), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoImg)
        f_lbl2.place(x=510, y=-80, width=515, height=270)

        img3 = Image.open(r"project_Images\student2.jpg")
        img3 = img3.resize((520, 130), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoImg3)
        f_lbl3.place(x=1020, y=-40, width=510, height=190)

        img1bg = Image.open(r"project_Images\background.PNG")
        img1bg = img1bg.resize((1570, 730), Image.ANTIALIAS)
        self.photoImg1bg = ImageTk.PhotoImage(img1bg)
        bg_lbl = Label(self.root, image=self.photoImg1bg)
        bg_lbl.place(x=0, y=120, width=1550, height=770)

        title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"),
                          bg="red", fg="black")
        title_lbl.place(x=-3, y=-1, width=1550, height=35)

# main frame
        mainFrame=Frame(bg_lbl,bd=2,bg="white")
        mainFrame.place(x=20,y=35,width=1500,height=620)

# left level frame
        leftFrame=LabelFrame(mainFrame,bd=2,bg="white",text="Student Detail",font=("times new roma",12,"bold"))
        leftFrame.place(x=25,y=7,width=720,height=590)


        img_left = Image.open(r"project_Images\student1.jpg")
        img_left = img_left.resize((730, 140), Image.ANTIALIAS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(leftFrame, image=self.photoImg_left)
        f_lbl_left.place(x=0, y=0, width=715, height=130)

# current course
        cuurent_course_Frame = LabelFrame(leftFrame, bd=2, bg="white", text="Current Course Information", font=("times new roma", 12, "bold"))
        cuurent_course_Frame.place(x=0, y=130, width=715, height=100)

    # Department
        dep_lebel=Label(cuurent_course_Frame,text="Department",bg="white",font=("times new roman",13,"bold"))
        dep_lebel.grid(row=0,column=2,padx=70,sticky=W)

        dep_combo=ttk.Combobox(cuurent_course_Frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=20,state="read only")
        dep_combo["values"]=("Select Department","CSE","IT","CE","EE","EC","ME","BT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=25,pady=4,sticky=W)

    # course
        course_lebel = Label(cuurent_course_Frame, text="Course", bg="white", font=("times new roman", 13, "bold"))
        course_lebel.grid(row=0, column=0,padx=15,sticky=W)

        course_combo = ttk.Combobox(cuurent_course_Frame,textvariable=self.var_course,font=("times new roman", 10, "bold"), width=20,
                                 state="read only")
        course_combo["values"] = ("Select Course","B.Tech","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=15, pady=4, sticky=W)

    # year
        year_lebel = Label(cuurent_course_Frame, text="Year", bg="white", font=("times new roman", 13, "bold"))
        year_lebel.grid(row=1, column=0,padx=15,sticky=W)

        year_combo = ttk.Combobox(cuurent_course_Frame,textvariable=self.var_year ,font=("times new roman", 10, "bold"), width=20,
                                 state="read only")
        year_combo["values"] = ("Select Year","2019-23","2020-24","2021-25", "2022-26", "2023-27", "2024-28", "2025-29", "2026-30")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=16, pady=7, sticky=W)

    # Semester
        sem_lebel = Label(cuurent_course_Frame, text="Semester", bg="white", font=("times new roman", 13, "bold"))
        sem_lebel.grid(row=1, column=2, padx=70,sticky=W)

        sem_combo = ttk.Combobox(cuurent_course_Frame,textvariable=self.var_semester, font=("times new roman", 10, "bold"), width=20,
                                 state="read only")
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=25, pady=7, sticky=W)

# class student information
        class_student_Frame = LabelFrame(leftFrame, bd=2, bg="white", text="Class Student Information", font=("times new roma", 12, "bold"))
        class_student_Frame.place(x=0, y=230, width=715, height=325)
    #student id
        student_id_lebel = Label(class_student_Frame, text="Student Id", bg="white", font=("times new roman", 13, "bold"))
        student_id_lebel.grid(row=0, column=0, padx=15,sticky=W)

        studentIdEntry=ttk.Entry(class_student_Frame,width=20,textvariable=self.var_stdId,font=("times new roman", 13, "bold"))
        studentIdEntry.grid(row=0,column=1,padx=15,pady=5,sticky=W)

    # student name
        studentName_label= Label(class_student_Frame, text="Student Name", bg="white", font=("times new roman", 13, "bold"))
        studentName_label.grid(row=0, column=2, padx=25, sticky=W)

        studentNameEntry = ttk.Entry(class_student_Frame, width=20,textvariable=self.var_stdName, font=("times new roman", 13, "bold"))
        studentNameEntry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

    # class divisio
        classDivision_lebel = Label(class_student_Frame, text="Class Division", bg="white",font=("times new roman", 13, "bold"))
        classDivision_lebel.grid(row=1, column=0, padx=15, sticky=W)

        div_combo = ttk.Combobox(class_student_Frame, textvariable=self.var_div,font=("times new roman", 10, "bold"), width=23,state="read only")
        div_combo["values"] = ("Select Division", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=15, pady=4, sticky=W)

    # Roll number
        roolNumber_label = Label(class_student_Frame, text="Roll Number", bg="white",
                                  font=("times new roman", 13, "bold"))
        roolNumber_label.grid(row=1, column=2, padx=25, sticky=W)

        roolNumberEntry = ttk.Entry(class_student_Frame, width=20,textvariable=self.var_roll,font=("times new roman", 13, "bold"))
        roolNumberEntry.grid(row=1, column=3, padx=0, pady=15, sticky=W)
    # gender
        gender_lebel = Label(class_student_Frame, text="Gender", bg="white", font=("times new roman", 13, "bold"))
        gender_lebel.grid(row=2, column=0, padx=15, sticky=W)

        gender_combo = ttk.Combobox(class_student_Frame,textvariable=self.var_gender,font=("times new roman", 10, "bold"), width=23,
                                 state="read only")
        gender_combo["values"] = ("Select Gender","Male","Femail","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=15, pady=4, sticky=W)

    # Dob
        dob_label = Label(class_student_Frame, text="DOB", bg="white",
                                 font=("times new roman", 13, "bold"))
        dob_label.grid(row=2, column=2, padx=25, sticky=W)

        dobEntry = ttk.Entry(class_student_Frame, width=20,textvariable=self.var_dob, font=("times new roman", 13, "bold"))
        dobEntry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
    # Email
        Email_lebel = Label(class_student_Frame, text="Email", bg="white",
                                 font=("times new roman", 13, "bold"))
        Email_lebel.grid(row=3, column=0, padx=15, sticky=W)

        EmailEntry = ttk.Entry(class_student_Frame,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        EmailEntry.grid(row=3 ,column=1, padx=15, pady=5, sticky=W)

    # phne number
        phoneNo_label = Label(class_student_Frame, text="Phone No", bg="white",
                          font=("times new roman", 13, "bold"))
        phoneNo_label.grid(row=3, column=2, padx=25, sticky=W)

        phoneNoEntry = ttk.Entry(class_student_Frame, width=20,textvariable=self.var_phone, font=("times new roman", 13, "bold"))
        phoneNoEntry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

    # address
        address_lebel = Label(class_student_Frame, text="Address", bg="white",
                                 font=("times new roman", 13, "bold"))
        address_lebel.grid(row=4, column=0, padx=15, sticky=W)

        addressEntry = ttk.Entry(class_student_Frame, width=20,textvariable=self.var_address, font=("times new roman", 13, "bold"))
        addressEntry.grid(row=4 ,column=1, padx=15, pady=5, sticky=W)

    # Teacher name
        teacher_label = Label(class_student_Frame, text="Teacher Name", bg="white",
                          font=("times new roman", 13, "bold"))
        teacher_label.grid(row=4, column=2, padx=25, sticky=W)

        teacherEntry = ttk.Entry(class_student_Frame, width=20,textvariable=self.var_teacher ,font=("times new roman", 13, "bold"))
        teacherEntry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

    # radio button
        self.var_rad1=StringVar()
        radioBtn1=ttk.Radiobutton(class_student_Frame,variable=self.var_rad1,text="Take photo sample",value="yes")
        radioBtn1.grid(row=5,column=0)

        radioBtn2 =ttk.Radiobutton(class_student_Frame,variable=self.var_rad1,text="No photo sample", value="No")
        radioBtn2.grid(row=5, column=1)

# button frame
        btn1_Frame = LabelFrame(class_student_Frame, bd=2, bg="white",relief=RIDGE)
        btn1_Frame.place(x=0, y=225, width=710, height=75)

    #save button
        saveBtn=Button(btn1_Frame,text="Save",width=18,height=1,command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        saveBtn.grid(row=0,column=0)
    #Update buttton
        updateBtn = Button(btn1_Frame, text="Update", width=18,command=self.update_data,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        updateBtn.grid(row=0, column=1)
    # dillit button
        deleteBtn = Button(btn1_Frame, text="Delete", width=17,command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        deleteBtn.grid(row=0, column=2)
    # reset buttton
        resetBtn = Button(btn1_Frame, text="Reset", width=17, command=self.reset_data,font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        resetBtn.grid(row=0, column=3)

        btn2_frame = LabelFrame(class_student_Frame, bd=2, bg="white", relief=RIDGE)
        btn2_frame.place(x=0, y=260, width=710, height=35)

        takephoto_Btn = Button(btn2_frame, text="Take Photo sample", command=self.generate_dataSet, width=37,pady=3, font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        takephoto_Btn.grid(row=0, column=0)

        updatephoto_Btn = Button(btn2_frame, text="Update Photo sample",width=38, pady=3,command=self.generate_dataSet,
                               font=("times new roman", 13, "bold"), bg="blue",
                               fg="white")
        updatephoto_Btn.grid(row=0, column=1)


# right level frame
        rightFrame = LabelFrame(mainFrame, bd=2, bg="white", text="Student Detail", font=("times new roma", 12, "bold"))
        rightFrame.place(x=750, y=7, width=720, height=590)

        img_right = Image.open(r"project_Images\student4.jpg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoImg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = Label(rightFrame, image=self.photoImg_right)
        f_lbl_right.place(x=0, y=0, width=715, height=125)

        # =============searching frame=================
        search_Frame = LabelFrame(rightFrame, bd=2, bg="white", text="Search System",
                                         font=("times new roma", 12, "bold"))
        search_Frame.place(x=0, y=135, width=712, height=65)

        search_label = Label(search_Frame, text="Search By", bg="red",fg="white",
                              font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=5, sticky=W)


        search_combo = ttk.Combobox(search_Frame, font=("times new roman", 10, "bold"), width=15,state="read only")
        search_combo["values"] = ("Select here", "Roll Number", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, sticky=W)

        searchEntry = ttk.Entry(search_Frame, width=20, font=("times new roman", 13, "bold"))
        searchEntry.grid(row=0, column=2,sticky=W)

        searchBtn = Button(search_Frame, text="Search", width=11, font=("times new roman", 11, "bold"), bg="blue",
                           fg="white")
        searchBtn.grid(row=0, column=3,padx=5)

        showAll = Button(search_Frame, text="Show All", width=11, font=("times new roman", 11, "bold"), bg="blue",
                           fg="white")
        showAll.grid(row=0, column=4)

        #===table frame===========================================

        table_Frame =Frame(rightFrame, bd=2, bg="white",relief=RIDGE)
        table_Frame.place(x=0, y=205, width=710, height=360)

        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_Frame,columns=("dep","course","year","sem","Id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("Id", text="StudentId")
        self.student_table.heading("name", text="StudentName")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)


        self.student_table.column("dep",width=80)
        self.student_table.column("course", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("sem", width=80)
        self.student_table.column("Id", width=120)
        self.student_table.column("name",width=150)
        self.student_table.column("gender", width=80)
        self.student_table.column("div", width=80)
        self.student_table.column("roll", width=150)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #==============================================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or \
                self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester"or\
                self.var_stdId.get()=="" or self.var_stdName.get()=="" or self.var_div.get()=="" or \
                self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_gender.get()=="Select Gender":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
                mycursor=conn.cursor()
                sql = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_stdId.get(),
                       self.var_stdName.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),
                       self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_rad1.get())
                mycursor.execute(sql, val)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes","Student detail has been added succesfully ",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Eroor",f" Due to :{str(es)}",parent=self.root)

# =============================================

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def search_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


# =============================================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stdId.set(data[4]),
        self.var_stdName.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_rad1.set(data[14])

# update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or \
                self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester"or\
                self.var_stdId.get()=="" or self.var_stdName.get()=="" or self.var_div.get()=="" or \
                self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_gender.get()=="Select Gender":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update > 0:
                    conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Dep=%s,Course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSamle=%s where StudentId=%s",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_stdName.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_rad1.get(),
                                                                                                        self.var_stdId.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student details succesfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
#delete data
    def delete_data(self):
        if self.var_stdId.get()=="":
            messagebox.showerror("Eroor","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
                mycursor = conn.cursor()
                if delete>0:
                    sql="delete from student where StudentId=%s"
                    val=(self.var_stdId.get())
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student detail deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


# reset data from table
    def reset_data(self):
        self.var_div.set("Select Division")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_gender.set("Select Gender")
        self.var_stdId.set("")
        self.var_stdName.set("")
        self.var_roll.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_rad1.set("")

    def generate_dataSet(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or \
                self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or \
                self.var_stdId.get() == "" or self.var_stdName.get() == "" or self.var_div.get() == "" or \
                self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_gender.get() == "Select Gender":
            messagebox.showerror("Error", "All field are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="3121",database="facerecognizer")
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myResult = mycursor.fetchall()
                id = 0
                for x in myResult:
                    id += 1
                mycursor.execute("update student set Dep=%s,Course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSamle=%s where StudentId=%s",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_stdName.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_rad1.get(),
                                                                                        self.var_stdId.get()==id+1
                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ====================load pre define data on face frontal from open cv =======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor=1.3 minimum neighbour=5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                imgId = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        imgId += 1
                        face = cv2.resize(face_cropped(my_frame), (650, 550))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(imgId) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(imgId),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)
                    if cv2.waitKey(1) == 13 or int(imgId) == 20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed successfully!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()