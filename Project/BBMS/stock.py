from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql

class bbms3:
    def __init__(self,root):
        self.root=root
       # self.root.title("Blood Bank Management System".center(550))
        self.root.iconbitmap("")
        self.root.title("Blood Bank Management System".center(330))
        self.root.geometry('1270x600+0+0')
        self.root.configure(background="#f50b07")
        title=Label(self.root,text="STOCK INFORMATION",font=("aldus",40,"bold"),bd=10,fg="#e86464",bg="#423e3e",width=50).pack()

        donor_Frame = LabelFrame(self.root, text="ADD BLOOD", bd=10, relief=RIDGE,
                                 font=("Calisto MT", 20, "bold"), fg="#e86464", bg="#423e3e")
        donor_Frame.place(x=20, y=100, width=440, height=550)

        self.sid = StringVar()
        #self.sbid = StringVar()
        self.sbg = StringVar()
        self.status= StringVar()
        self.quantity =StringVar()
        self.hname = StringVar()
        self.hadd = StringVar()
        self.hphn = StringVar()

        st_id = Label(donor_Frame, text="Stock Id", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        e_id = Entry(donor_Frame, textvariable=self.sid, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e_id.grid(row=1, column=1, pady=0, padx=0, sticky="w")

        '''st_bid = Label(donor_Frame, text="Blood Id", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_bid.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        e2_bid = Entry(donor_Frame, textvariable=self.sbid, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e2_bid.grid(row=2, column=1, pady=10, padx=0, sticky="w")

        opt_bid = ttk.Combobox(donor_Frame, textvariable=self.sbid, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_bid['values'] = ("101 [A+]", "102 [A-]", "103 [B+]", "104 [B-]", "105 [O+]", "106 [O-]", "107 [AB+]", "109 [AB-]")
        opt_bid.grid(row=2, column=1, pady=10, padx=0)'''

        st_bg = Label(donor_Frame, text="Blood Group", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_bg.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        e3_bg = Entry(donor_Frame, textvariable=self.sbg, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e3_bg.grid(row=2, column=1, pady=0, padx=0, sticky="w")

        opt_bg = ttk.Combobox(donor_Frame, textvariable=self.sbg, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_bg['values'] = ("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
        opt_bg.grid(row=2, column=1, pady=10, padx=0)

        st_status = Label(donor_Frame, text="Blood Status", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        st_status.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        e4_status = Entry(donor_Frame, textvariable=self.status, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e4_status.grid(row=3, column=1, pady=10, padx=0, sticky="w")

        opt_status = ttk.Combobox(donor_Frame, textvariable=self.status, font=("Calisto MT", 12, "bold"), state='readonly')
        opt_status['values'] = ("Availavle","Not Availavle")
        opt_status.grid(row=3, column=1, pady=10, padx=0)

        quantity = Label(donor_Frame, text="Quantity", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        quantity.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        e5_quantity = Entry(donor_Frame, textvariable=self.quantity, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e5_quantity.grid(row=4, column=1, pady=10, padx=0, sticky="w")

        H_name = Label(donor_Frame, text="Hospital Name", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        H_name.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        e6_Hname = Entry(donor_Frame, textvariable=self.hname, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e6_Hname.grid(row=5, column=1, pady=10, padx=0, sticky="w")

        H_add = Label(donor_Frame, text="Hospital Address", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        H_add.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        e7_Hadd = Entry(donor_Frame, textvariable=self.hadd, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e7_Hadd.grid(row=6, column=1, pady=10, padx=0, sticky="w")

        H_cont = Label(donor_Frame, text="Hospital Phn", bg="#423e3e", fg="#e86464", font=("Calisto MT", 15, "bold"))
        H_cont.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        e6_Hcont = Entry(donor_Frame, textvariable=self.hphn, font=("Calisto MT", 13, "bold"), bd=5, relief=GROOVE)
        e6_Hcont.grid(row=7, column=1, pady=10, padx=0, sticky="w")

        save_button = Button(donor_Frame, text="Add", font=("bookman", 13, "bold"), padx=20, fg="white", bg="#e86464",command=self.save)
        save_button.place(x=202, y=422, height=25)

        clear_button = Button(donor_Frame, text="Clear", font=("bookman", 13, "bold"), padx=18, fg="white",bg="#e86464",command=self.clear)
        clear_button.place(x=302, y=422, height=25)

        #stockframe

        stock_Frame = Frame(self.root, bd=10, relief=RIDGE, bg="#423e3e")
        stock_Frame.place(x=500, y=100, height=550, width=760)

        deletebtn = Button(stock_Frame, text="Delete", font=("bookman", 13, "bold"), padx=18, fg="white",
                           bg="#e86464",command=self.delete_Blood)
        deletebtn.place(x=515, y=500, height=25)

        updatebtn = Button(stock_Frame, text="Update", font=("bookman", 13, "bold"), padx=18, fg="white",
                           bg="#e86464",command=self.update_data)
        updatebtn.place(x=624, y=500, height=25)

        self.search_by = StringVar()
        self.search_here = StringVar()

        don_search = Label(stock_Frame, text="Search By :", bg="#423e3e", fg="#e86464",
                           font=("Calisto MT", 20, "bold"))
        don_search.grid(row=0, column=0, pady=0, padx=25, sticky="w")

        e10_search = Entry(stock_Frame, textvariable=self.search_by, font=("Calisto MT", 13, "bold"), bd=5,
                           relief=GROOVE)
        e10_search.grid(row=0, column=1, pady=10, padx=0, sticky="w")

        opt_search = ttk.Combobox(stock_Frame, textvariable=self.search_by, width=20,
                                  font=("Calisto MT", 12, "bold"), state='readonly')
        opt_search['values'] = ("Stock_id","Blood_Group","Hospital_Name")
        opt_search.grid(row=0, column=1, padx=4, pady=0)

        e11_Search = Entry(stock_Frame, textvariable=self.search_here, width=20, font=("Calisto MT", 14, "bold"),
                           bd=5, relief=GROOVE)
        e11_Search.grid(row=0, column=2, pady=10, padx=15, sticky="w")

        searchbtn = Button(stock_Frame, text="Search", width=10,command=self.search_data)
        searchbtn.grid(row=0, column=3)

        Table_Frame = Frame(stock_Frame, bd=4, relief=RIDGE, bg="#e86464")
        Table_Frame.place(x=10, y=60, width=720, height=435)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.stock_table = ttk.Treeview(Table_Frame,
                                           columns=(
                                           "sid","sbg", "status", "quantity", "hname", "hadd",
                                           "hphn"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.stock_table.xview)
        scroll_y.config(command=self.stock_table.yview)

        self.stock_table.heading("sid", text="Stock Id")
        #self.stock_table.heading("sbid", text="Blood Id")
        self.stock_table.heading("sbg", text="Blood Group")
        self.stock_table.heading("status", text="Status")
        self.stock_table.heading("quantity", text="Quantity")
        self.stock_table.heading("hname", text="Hospital Name")
        self.stock_table.heading("hadd", text="Hospital Address")
        self.stock_table.heading("hphn", text="Hospital Phone")


        self.stock_table['show'] = 'headings'

        self.stock_table.column("sid", width=70)
        #self.stock_table.column("sbid", width=70)
        self.stock_table.column("sbg", width=80)
        self.stock_table.column("status", width=90)
        self.stock_table.column("quantity", width=70)
        self.stock_table.column("hname", width=250)
        self.stock_table.column("hadd", width=250)
        self.stock_table.column("hphn", width=110)

        self.stock_table.pack(fill=BOTH, expand=1)
        self.stock_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def search_data(self):
        sercon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sercon.cursor()

        cur.execute(
            "select * from stock where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_here.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert('', END, values=row)
            sercon.commit()
        sercon.close()

    def save(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = sqlcon.cursor()
        cur.execute("insert into stock values(%s,%s,%s,%s,%s,%s,%s)", (
            self.sid.get(),
            #self.bid.get(),
            self.sbg.get(),
            self.status.get(),
            self.quantity.get(),
            self.hname.get(),
            self.hadd.get(),
            self.hphn.get()
        ))

        sqlcon.commit()
        self.fetch_data()
        self.clear()
        sqlcon.close()

    def fetch_data(self):
        felcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = felcon.cursor()
        cur.execute("Select * from stock")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert('', END, values=row)
            felcon.commit()
        felcon.close()

    def clear(self):
        self.sid.set("")
        #self.sbid.set("")
        self.sbg.set("")
        self.status.set("")
        self.quantity.set("")
        self.hname.set("")
        self.hadd.set("")
        self.hphn.set("")

    def get_cursor(self, ev):
        cursor_row = self.stock_table.focus()
        contents = self.stock_table.item(cursor_row)
        row = contents['values']

        self.sid.set(row[0])
        #self.sbid.set(row[1])
        self.sbg.set(row[1])
        self.status.set(row[2])
        self.quantity.set(row[3])
        self.hname.set(row[4])
        self.hadd.set(row[5])
        self.hphn.set(row[6])

    def delete_Blood(self):
        delcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = delcon.cursor()
        cur.execute("delete from stock where Stock_id=%s", self.sid.get())

        delcon.commit()
        delcon.close()
        self.fetch_data()
        self.clear()

    def update_data(self):
        updcon = pymysql.connect(host="localhost", user="root", password="", database="bbms")
        cur = updcon.cursor()
        cur.execute("update stock set Blood_Group=%s,Stock_status=%s,Stock_Quantity=%s,Hospital_Name=%s,Hospital_Address=%s,Hospital_Phone=%s where Stock_id=%s",(

            #self.sbid.get(),
            self.sbg.get(),
            self.status.get(),
            self.quantity.get(),
            self.hname.get(),
            self.hadd.get(),
            self.hphn.get(),
            self.sid.get()


        ))

        updcon.commit()
        self.fetch_data()
        self.clear()
        updcon.close()

root = Tk()
ss = bbms3(root)
root.mainloop()