from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql


class bbms6:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#ffa31a")
        title=Label(self.root,text="Blood Bank Management System",font=("aldus",40,"bold"),bd=10,fg="#ffa31a",bg="#423e3e",width=50).pack()

        sign_Frame=LabelFrame(self.root,text="Sign up",bd=10,font=("bookman",20,"bold"), relief=RIDGE,fg="White",bg="#423e3e")
        sign_Frame.place(x=360, y=155, width=525, height=430)

        self.fname=StringVar()
        self.lname = StringVar()
        self.username=StringVar()
        self.bg=StringVar()
        self.email=StringVar()
        self.phone=StringVar()
        self.passw=StringVar()
        self.cpassw=StringVar()

        fname = Label(sign_Frame, text="First Name", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        fname.grid(row=1, column=0, pady=0, padx=10, sticky="w")

        e_fname = Entry(sign_Frame, textvariable=self.fname, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,width=25)
        e_fname.grid(row=2, column=0, pady=0, padx=10, sticky="w")

        lname = Label(sign_Frame, text="Last Name", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        lname.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        e_lname = Entry(sign_Frame, textvariable=self.lname, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_lname.grid(row=2, column=1, pady=0, padx=10, sticky="w")

        uname = Label(sign_Frame, text="User Name", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        uname.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        e_uname = Entry(sign_Frame, textvariable=self.username, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_uname.grid(row=4, column=0, pady=0, padx=10, sticky="w")

        bg = Label(sign_Frame, text="Blood Group", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        bg.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        e_bg = Entry(sign_Frame, textvariable=self.bg, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,width=25)
        e_bg.grid(row=4, column=1, pady=0, padx=10, sticky="w")

        opt1_bg = ttk.Combobox(sign_Frame, textvariable=self.bg, font=("Calisto MT", 12, "bold"), state='readonly',width=26)
        opt1_bg['values'] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        opt1_bg.grid(row=4, column=1, pady=0, padx=10)

        email = Label(sign_Frame, text="Email", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        email.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        e_email = Entry(sign_Frame, textvariable=self.email, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_email.grid(row=6, column=0, pady=0, padx=10, sticky="w")

        phone = Label(sign_Frame, text="Phone", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        phone.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        e_phone = Entry(sign_Frame, textvariable=self.phone, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_phone.grid(row=6, column=1, pady=0, padx=10, sticky="w")

        passw = Label(sign_Frame, text="Password", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        passw.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        e_passw = Entry(sign_Frame, textvariable=self.passw, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_passw.grid(row=8, column=0, pady=0, padx=10, sticky="w")

        cpassw = Label(sign_Frame, text="Confirm Password", bg="#423e3e", fg="#ffa31a", font=("Calisto MT", 15, "bold"))
        cpassw.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        e_cpassw = Entry(sign_Frame, textvariable=self.passw, font=("Calisto MT", 13, "bold"), bd=3, relief=GROOVE,
                        width=25)
        e_cpassw.grid(row=8, column=1, pady=0, padx=10, sticky="w")

        sign_button = Button(sign_Frame, text="Sign up", font=("bookman", 20, "bold"), padx=120, fg="white",
                             bg="#ffa31a")
        sign_button.place(x=80, y=325, height=40, width=340)



root = Tk()
ss = bbms6(root)
root.mainloop()