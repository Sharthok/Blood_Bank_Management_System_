from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql

class bbms2:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System".center(330))
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#f50b07")
        title=Label(self.root,text="DONOR INFORMATION",font=("aldus",40,"bold"),bd=10,fg="#e86464",bg="#423e3e",width=50).pack()

        self.did= StringVar()
        self.dname= StringVar()
        self.dbg = StringVar()
        self.dage = StringVar()
        self.dgender= StringVar()
        self.dcontact= StringVar()
        self.daddress = StringVar()
        self.dlast_donate = StringVar()
        self.dnext_donate= StringVar()

        donor_Frame = LabelFrame(self.root,text="Donor Registration", bd=10, relief=RIDGE,font=("Calisto MT", 20, "bold"),fg="#e86464", bg="#423e3e")
        donor_Frame.place(x=20, y=100, width=440, height=550)


        #m_title = Label(donor_Frame, text="Donor Registration", bg="#e86464", fg="black", font=("Calisto MT", 20, "bold"))
        #m_title.grid(row=0, columnspan=2, padx=80,pady=10)

        dn_id = Label(donor_Frame, text="Donor Id", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        e_id = Entry(donor_Frame, textvariable=self.did, font=("Calisto MT", 13, "bold"), bd=5,relief=GROOVE)
        e_id.grid(row=1, column=1, pady=0, padx=0, sticky="w")

        dn_name = Label(donor_Frame, text="Donor Name", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        e2_name = Entry(donor_Frame, textvariable=self.dname, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e2_name.grid(row=2, column=1, pady=10, padx=0, sticky="w")

        dn_bg = Label(donor_Frame, text="Blood Group", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_bg.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        e3_bg = Entry(donor_Frame, textvariable=self.dbg, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e3_bg.grid(row=3, column=1, pady=0, padx=0, sticky="w")

        opt_bg = ttk.Combobox(donor_Frame, textvariable=self.dbg, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_bg['values'] = ("A+","A-","B+","B-","O+","O-","AB+","AB-")
        opt_bg.grid(row=3, column=1, pady=10, padx=0)

        dn_age = Label(donor_Frame, text="Donor Age", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_age.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        e4_age = Entry(donor_Frame, textvariable=self.dage, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e4_age.grid(row=4, column=1, pady=10, padx=0, sticky="w")

        dn_gender = Label(donor_Frame, text="Donor Gender", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        e5_gender = Entry(donor_Frame, textvariable=self.dgender, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e5_gender.grid(row=5, column=1, pady=10, padx=0, sticky="w")

        opt_gender = ttk.Combobox(donor_Frame, textvariable=self.dgender, font=("Calisto MT", 12, "bold"),state='readonly')
        opt_gender['values'] = ("Male", "Female", "Other")
        opt_gender.grid(row=5, column=1, pady=10, padx=0)

        dn_cnt = Label(donor_Frame, text="Donor Phn", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_cnt.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        e6_cnt = Entry(donor_Frame, textvariable=self.dcontact, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e6_cnt.grid(row=6, column=1, pady=10, padx=0, sticky="w")

        dn_ld = Label(donor_Frame, text="Last Donate", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_ld.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        e7_ld = Entry(donor_Frame, textvariable=self.dlast_donate, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e7_ld.grid(row=7, column=1, pady=10, padx=0, sticky="w")

        dn_nd = Label(donor_Frame, text="Next Donate avl.", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_nd.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        e8_nd = Entry(donor_Frame, textvariable=self.dnext_donate, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e8_nd.grid(row=8, column=1, pady=10, padx=0, sticky="w")

        dn_add = Label(donor_Frame, text="Donor Address", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        dn_add.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        e9_add = Entry(donor_Frame, textvariable=self.daddress, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e9_add.grid(row=9, column=1, pady=10, padx=0, sticky="w")


        save_button = Button(donor_Frame, text="Save", font=("bookman", 13, "bold"), padx=20, fg="white", bg="#e86464",command=self.save)
        save_button.place(x=202, y=465, height=25)

        clear_button = Button(donor_Frame, text="Clear", font=("bookman", 13, "bold"), padx=18, fg="white", bg="#e86464",command=self.clear)
        clear_button.place(x=302, y=465, height=25)


        #donor databaase
        database_Frame=Frame(self.root, bd=10, relief=RIDGE, bg="#423e3e")
        database_Frame.place(x=500, y=100,height=550,width=760)

        deletebtn = Button(database_Frame, text="Delete",font=("bookman", 13, "bold"), padx=18,fg="white", bg="#e86464",command=self.delete_donor)
        deletebtn.place(x=515,y=500,height=25)

        updatebtn = Button(database_Frame, text="Update", font=("bookman", 13, "bold"), padx=18, fg="white",bg="#e86464",command=self.update_data)
        updatebtn.place(x=624, y=500, height=25)



        self.search_by = StringVar()
        self.search_here = StringVar()

        don_search = Label(database_Frame, text="Search By :", bg="#423e3e", fg="#e86464", font=("Calisto MT", 20, "bold"))
        don_search.grid(row=0, column=0, pady=0, padx=25, sticky="w")

        e10_search = Entry(database_Frame, textvariable=self.search_by, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e10_search.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        opt_search = ttk.Combobox(database_Frame, textvariable=self.search_by, width=20,
                                    font=("Calisto MT", 12, "bold"), state='readonly')
        opt_search['values'] = ("D_Id", "D_Name", "D_Blood_Group")
        opt_search.grid(row=0, column=1, padx=4, pady=0)

        e11_Search = Entry(database_Frame, textvariable=self.search_here, width=20, font=("Calisto MT", 14, "bold"),bd=5, relief=GROOVE)
        e11_Search.grid(row=0, column=2, pady=10, padx=15, sticky="w")

        searchbtn = Button(database_Frame, text="Search", width=10,command=self.search_data)
        searchbtn.grid(row=0,column=3)

        Table_Frame = Frame(database_Frame, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame.place(x=10, y=60, width=720, height=435)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.database_table = ttk.Treeview(Table_Frame,
                    columns=("did", "dname","dbg", "dage", "dgender", "dcontact","dlast_donate","dnext_donate","daddress"),
                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.database_table.xview)
        scroll_y.config(command=self.database_table.yview)

        self.database_table.heading("did", text="Donor Id")
        self.database_table.heading("dname", text="Name")
        self.database_table.heading("dbg", text="Blood Group")
        self.database_table.heading("dage", text="Age")
        self.database_table.heading("dgender", text="Gender")
        self.database_table.heading("dcontact", text="Phone")
        self.database_table.heading("dlast_donate", text="Last Donate")
        self.database_table.heading("dnext_donate", text="Next Donate Avl")
        self.database_table.heading("daddress", text="Address")

        self.database_table['show'] = 'headings'

        self.database_table.column("did", width=60)
        self.database_table.column("dname", width=180)
        self.database_table.column("dbg", width=80)
        self.database_table.column("dage",width=70)
        self.database_table.column("dgender", width=70)
        self.database_table.column("dcontact", width=110)
        self.database_table.column("daddress", width=210)
        self.database_table.column("dlast_donate", width=110)
        self.database_table.column("dnext_donate", width=110)

        self.database_table.pack(fill=BOTH, expand=1)
        self.database_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def search_data(self):
        sercon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sercon.cursor()

        cur.execute("select * from donor where "+str(self.search_by.get())+" LIKE '%"+str(self.search_here.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.database_table.delete(*self.database_table.get_children())
            for row in rows:
                self.database_table.insert('', END, values=row)
            sercon.commit()
        sercon.close()

    def save (self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sqlcon.cursor()
        cur.execute("insert into donor values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.did.get(),
            self.dname.get(),
            self.dbg.get(),
            self.dage.get(),
            self.dgender.get(),
            self.dcontact.get(),
            self.dlast_donate.get(),
            self.dnext_donate.get(),
            self.daddress.get()
        ))

        sqlcon.commit()
        self.fetch_data()
        self.clear()
        sqlcon.close()


    def fetch_data(self):
        felcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = felcon.cursor()
        cur.execute("Select * from donor")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.database_table.delete(*self.database_table.get_children())
            for row in rows:
                self.database_table.insert('', END, values=row)
            felcon.commit()
        felcon.close()

    def clear(self):
        self.did.set("")
        self.dname.set("")
        self.dbg.set("")
        self.dage.set("")
        self.dgender.set("")
        self.dcontact.set("")
        self.dlast_donate.set("")
        self.dnext_donate.set("")
        self.daddress.set("")

    def get_cursor(self, ev):
        cursor_row = self.database_table.focus()
        contents = self.database_table.item(cursor_row)
        row = contents['values']

        self.did.set(row[0])
        self.dname.set(row[1])
        self.dbg.set(row[2])
        self.dage.set(row[3])
        self.dgender.set(row[4])
        self.dcontact.set(row[5])
        self.dlast_donate.set(row[6])
        self.dnext_donate.set(row[7])
        self.daddress.set(row[8])

    def delete_donor(self):
        delcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = delcon.cursor()
        cur.execute("delete from donor where D_Id=%s", self.did.get())

        delcon.commit()
        delcon.close()
        self.fetch_data()
        self.clear()

    def update_data(self):
        updcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = updcon.cursor()
        cur.execute("update donor set D_Name=%s,D_Blood_Group=%s,D_Age=%s,D_Gender=%s,D_Phone=%s,D_Last_Donate=%s,D_Next_Donate=%s,D_Address=%s where D_Id=%s",(

            self.dname.get(),
            self.dbg.get(),
            self.dage.get(),
            self.dgender.get(),
            self.dcontact.get(),
            self.dlast_donate.get(),
            self.dnext_donate.get(),
            self.daddress.get(),
            self.did.get()

        ))

        updcon.commit()
        self.fetch_data()
        self.clear()
        updcon.close()



root = Tk()
ss = bbms2(root)
root.mainloop()