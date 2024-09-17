from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2
from cv2 import*
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 25, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=-3, y=-1, width=1530, height=35)

        img_top = Image.open(r"project_Images\facerecoginition.PNG")
        img_top = img_top.resize((1530, 350), Image.ANTIALIAS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)
        f_lbl_left = Label(self.root, image=self.photoImg_top)
        f_lbl_left.place(x=0, y=35, width=1530, height=300)

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", borderwidth=3,
                      font=("times new roman", 25, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=330, width=1530, height=55)

        img_bottom = Image.open(r"project_Images\gatheredPic.jpg")
        img_bottom = img_bottom.resize((1530, 390), Image.ANTIALIAS)
        self.photoImg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_left = Label(self.root, image=self.photoImg_bottom)
        f_lbl_left.place(x=0, y=380, width=1530, height=380)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        # ============================Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xls")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data set completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
