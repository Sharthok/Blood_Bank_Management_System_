from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql

class bbms1:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#b30000")
        title=Label(self.root,text="   BLOOD INFORMATION",font=("aldus",40,"bold"),bd=10,fg="#e86464",bg="#423e3e",width=50).pack()

        blood_Frame1 = LabelFrame(self.root, text="Common Blood types", bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#423e3e")
        blood_Frame1.place(x=40, y=170, width=580, height=370)

        heading1_frame1 = Label(blood_Frame1, text="Blood Group", fg="white", bg="#e86464", font=("Calisto MT", 15, "bold"))
        heading1_frame1.grid(row=1, column=0, pady=15, padx=20, sticky="w")

        heading2_frame1 = Label(blood_Frame1, text="Antigen", fg="white", bg="#e86464",width=28,font=("Calisto MT", 15, "bold"))
        heading2_frame1.grid(row=1, column=1, pady=15, padx=20, sticky="w")

        value1_frame1 = Label(blood_Frame1, text="A", bg="#423e3e", fg="#e86464",font=("Calisto MT", 15, "bold"))
        value1_frame1.grid(row=2, column=0, pady=5, padx=50, sticky="w")

        value2_frame1 = Label(blood_Frame1, text="B", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        value2_frame1.grid(row=3, column=0, pady=5, padx=50, sticky="w")

        value3_frame1 = Label(blood_Frame1, text="O", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        value3_frame1.grid(row=4, column=0, pady=5, padx=50, sticky="w")

        value4_frame1 = Label(blood_Frame1, text="AB", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        value4_frame1.grid(row=5, column=0, pady=5, padx=45, sticky="w")

        Avalue1_frame1 = Label(blood_Frame1, text="Red Cells: A antigen\nPlasma: B antibody", bg="#423e3e", fg="white", width=28,padx=0,font=("Calisto MT", 15, "bold"))
        Avalue1_frame1.grid(row=2, column=1, pady=5, padx=0, sticky="w")

        Avalue2_frame1 = Label(blood_Frame1, text="Red Cells: B antigen\nPlasma: A antibody", bg="#423e3e", fg="white",width=28,padx=0,font=("Calisto MT", 15, "bold"))
        Avalue2_frame1.grid(row=3, column=1, pady=5, padx=0, sticky="w")

        Avalue3_frame1 = Label(blood_Frame1, text="Red Cells: A & B antigen\nPlasma: No antibody", bg="#423e3e", fg="white",width=28,padx=0,font=("Calisto MT", 15, "bold"))
        Avalue3_frame1.grid(row=4, column=1, pady=5, padx=0, sticky="w")

        Avalue4_frame1 = Label(blood_Frame1, text="Red Cells:No antigen\nPlasma:A & B antibody", bg="#423e3e", fg="white",width=28,padx=0,font=("Calisto MT", 15,"bold"))
        Avalue4_frame1.grid(row=5, column=1, pady=5, padx=0, sticky="w")


        blood_Frame2 = LabelFrame(self.root, text="Compatitible Blood Type Donors", bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#423e3e")
        blood_Frame2.place(x=655, y=140, width=580, height=415)

        Table_Frame = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame.place(x=0, y=10, width=558, height=35)

        heading1_frame2 = Label(Table_Frame, text="Blood Group", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        heading1_frame2.grid(row=1, column=0, pady=0, padx=0, sticky="w")

        heading2_frame2 = Label(Table_Frame, text="Donate Blood To", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        heading2_frame2.grid(row=1, column=1, pady=0, padx=35, sticky="w")

        heading3_frame2 = Label(Table_Frame, text="Receive Blood From", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        heading3_frame2.grid(row=1, column=2, pady=0, padx=0, sticky="w")

        Table_Frame2 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame2.place(x=0, y=50, width=558, height=35)


        value1_frame2 = Label(Table_Frame2, text="A+", fg="white", bg="#e86464",
                                font=("Calisto MT", 15, "bold"))
        value1_frame2.grid(row=2, column=0, pady=0, padx=0, sticky="w")

        value12_frame2 = Label(Table_Frame2, text="A+ , AB+", fg="white", bg="#e86464",
                                font=("Calisto MT", 13, "bold"))
        value12_frame2.grid(row=2, column=1, pady=0, padx=145, sticky="w")

        value13_frame2 = Label(Table_Frame2, text="  A+ , A- , O+ , O-", fg="white", bg="#e86464",
                                font=("Calisto MT", 13, "bold"))
        value13_frame2.grid(row=2, column=2, pady=0, padx=0, sticky="w")


        Table_Frame3 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame3.place(x=0, y=87, width=558, height=35)

        value2_frame2 = Label(Table_Frame3, text="A-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=3, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame3, text="A+ , A- , AB+ , AB-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=3, column=1, pady=0, padx=149, sticky="w")

        value23_frame2 = Label(Table_Frame3, text="  A- , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=3, column=2, pady=0, padx=0, sticky="w")

        Table_Frame4 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame4.place(x=0, y=124, width=558, height=35)

        value2_frame2 = Label(Table_Frame4, text="B+", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=3, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame4, text="B+ , AB+", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=3, column=1, pady=0, padx=148, sticky="w")

        value23_frame2 = Label(Table_Frame4, text="B+ , B- , O+, O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=3, column=2, pady=0, padx=18, sticky="w")

        Table_Frame4 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame4.place(x=0, y=161, width=558, height=35)

        value2_frame2 = Label(Table_Frame4, text="B-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=4, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame4, text=" B+ , B- , AB+ , AB-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=4, column=1, pady=0, padx=150, sticky="w")

        value23_frame2 = Label(Table_Frame4, text="   B- , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=4, column=2, pady=0, padx=0, sticky="w")

        Table_Frame5 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame5.place(x=0, y=198, width=558, height=35)

        value2_frame2 = Label(Table_Frame5, text="O+", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=5, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame5, text="O+ , A+ , B+ , AB+", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=5, column=1, pady=0, padx=145, sticky="w")

        value23_frame2 = Label(Table_Frame5, text=" O+ , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=5, column=2, pady=0, padx=0, sticky="w")

        Table_Frame6 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame6.place(x=0, y=235, width=558, height=35)

        value2_frame2 = Label(Table_Frame6, text="O-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=6, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame6, text="Everyone", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=6, column=1, pady=0, padx=150, sticky="w")

        value23_frame2 = Label(Table_Frame6, text="  O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=6, column=2, pady=0, padx=80, sticky="w")

        Table_Frame7 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame7.place(x=0, y=272, width=558, height=35)

        value2_frame2 = Label(Table_Frame7, text="AB+", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=7, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame7, text="AB+", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=7, column=1, pady=0, padx=133, sticky="w")

        value23_frame2 = Label(Table_Frame7, text="Everyone", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=7, column=2, pady=0, padx=100, sticky="w")

        Table_Frame8 = Frame(blood_Frame2, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame8.place(x=0, y=309, width=558, height=35)

        value2_frame2 = Label(Table_Frame8, text="AB-", fg="white", bg="#e86464",
                              font=("Calisto MT", 15, "bold"))
        value2_frame2.grid(row=8, column=0, pady=0, padx=0, sticky="w")

        value22_frame2 = Label(Table_Frame8, text="AB+ , AB-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value22_frame2.grid(row=8, column=1, pady=0, padx=137, sticky="w")

        value23_frame2 = Label(Table_Frame8, text="   AB- , A- , B- , O-", fg="white", bg="#e86464",
                               font=("Calisto MT", 13, "bold"))
        value23_frame2.grid(row=8, column=2, pady=0, padx=0, sticky="w")


root = Tk()
ss = bbms1(root)
root.mainloop()