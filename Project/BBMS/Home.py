from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql

class bbms5:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System")
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#b30000")
        title=Label(self.root,text="HOME",font=("aldus",40,"bold"),bd=10,fg="#ffa31a",bg="#423e3e",width=50).pack()

        Home_Frame = LabelFrame(self.root,bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#ffa31a")
        Home_Frame.place(x=110, y=152, width=1070, height=320)

        Blood_button = Button(self.root, text="Blood\n Information", font=("bookman",20, "bold"), padx=20, fg="#ffa31a", bg="#333333",bd=10)
        Blood_button.place(x=225, y=200, height=225,width=240)

        Donor_button = Button(self.root, text="DONOR", font=("bookman", 20, "bold"), padx=20, fg="#ffa31a",bg="#333333", bd=10)
        Donor_button.place(x=525, y=200, height=225, width=240)

        Stock_button = Button(self.root, text="Stock\n Information", font=("bookman", 20, "bold"), padx=20, fg="#ffa31a",
                              bg="#333333", bd=10)
        Stock_button.place(x=825, y=200, height=225, width=240)

        mov = Label(self.root, text='"20 minuites of your time and 250 cc of your blood,may make the difference between life and death-"\n So donate blood and save life....!', bg="#b30000", fg="#ffffe6", font=("Calisto MT", 17, "bold"))
        mov.place(height=50,width=1070,y=500,x=110)




root = Tk()
ss = bbms5(root)
root.mainloop()