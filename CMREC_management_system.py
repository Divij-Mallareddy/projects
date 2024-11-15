from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from mysql import connector




class Student():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x900")
        self.root.title("CMREC's STUDENT BLOGS DATA")
        title =Label(self.root,text="STUDENT's BLOGS DATA",bd=20,font=('arial', 33, 'italic'),fg="navy")
        title.pack(side=TOP)
        #variables
        self.registration = StringVar()
        self.name = StringVar()
        self.contact = StringVar()
        self.branch = StringVar()
        self.first_year_1st_sem = StringVar()
        self.first_year_2nd_sem = StringVar()
        self.second_year_1st_sem =StringVar()
        self.second_year_2nd_sem = StringVar()
        self.third_year_1st_sem = StringVar()
        self.third_year_2nd_sem = StringVar()
        self.fourth_year_1st_sem = StringVar()
        self.fourth_year_2nd_sem = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()



        #Manage frame
        Manage_Frame = Frame(self.root, bd=6, relief="sunken", bg="blue")
        Manage_Frame.place(x=10, y=68, width=500, height=785)
        #registration
        register_no = Label(Manage_Frame, text="Register No",bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        register_no.grid(row=0, column=0, pady=8, padx=15)
        entry_registation_no = Entry(Manage_Frame, textvariable=self.registration, font=('times new roman', 10, "bold"), bd=2,
                         relief=GROOVE,width=40)
        entry_registation_no.grid(row=0, column=1, pady=8, padx=20,sticky="ew")
        entry_registation_no.grid_columnconfigure(0,weight=1)
        #name
        name = Label(Manage_Frame,text="Name",bg="blue",fg="white",
                     font=('times new roman',15,"bold"))
        name.grid(row=1,column=0,padx=15,pady=8)
        entry_name= Entry(Manage_Frame, textvariable=self.name, font=('times new roman', 10, "bold"),
                                     bd=2,
                                     relief=GROOVE, width=45)
        entry_name.grid(row=1, column=1, pady=8, padx=20, sticky="ew")
        entry_name.grid_columnconfigure(0, weight=1)
        #contact
        contact = Label(Manage_Frame, text="contact", bg="blue", fg="white",
                     font=('times new roman', 15, "bold"))
        contact.grid(row=2, column=0, padx=15, pady=8)
        entry_contact = Entry(Manage_Frame, textvariable=self.contact, font=('times new roman', 10, "bold"),
                           bd=2,
                           relief=GROOVE, width=45)
        entry_contact.grid(row=2, column=1, pady=8, padx=20, sticky="ew")
        entry_contact.grid_columnconfigure(0, weight=1)
        #branch
        branch = Label(Manage_Frame, text="Branch", bg="blue", fg="white",
                     font=('times new roman', 15, "bold"))
        branch.grid(row=3, column=0, padx=15, pady=8)
        entry_branch = Entry(Manage_Frame, textvariable=self.branch, font=('times new roman', 10, "bold"),
                           bd=2,
                           relief=GROOVE, width=45)
        entry_branch.grid(row=3, column=1, pady=8, padx=20, sticky="ew")
        entry_branch.grid_columnconfigure(0, weight=1)
        #first year
        year_1_1= Label(Manage_Frame, text="Frist_year_1st_sem", bg="blue", fg="white",
                     font=('times new roman', 15, "bold"))
        year_1_1.grid(row=4, column=0, padx=15, pady=8)
        entry_year_1_1= Entry(Manage_Frame, textvariable=self.first_year_1st_sem, font=('times new roman', 10, "bold"),
                           bd=2,
                           relief=GROOVE, width=45)
        entry_year_1_1.grid(row=4, column=1, pady=8, padx=20, sticky="ew")
        entry_year_1_1.grid_columnconfigure(0, weight=1)

        year_1_2 = Label(Manage_Frame, text="Frist_year_2nd_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_1_2.grid(row=5, column=0, padx=15, pady=8)
        entry_year_1_2 = Entry(Manage_Frame, textvariable=self.first_year_2nd_sem, font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_1_2.grid(row=5, column=1, pady=8, padx=20, sticky="ew")
        entry_year_1_2.grid_columnconfigure(0, weight=1)
        #second_year
        year_2_1 = Label(Manage_Frame, text="Second_year_1st_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_2_1.grid(row=6, column=0, padx=15, pady=8)
        entry_year_2_1 = Entry(Manage_Frame, textvariable=self.second_year_1st_sem, font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_2_1.grid(row=6, column=1, pady=8, padx=20, sticky="ew")
        entry_year_2_1.grid_columnconfigure(0, weight=1)

        year_2_2 = Label(Manage_Frame, text="Second_year_2st_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_2_2.grid(row=7, column=0, padx=15, pady=8)
        entry_year_2_2 = Entry(Manage_Frame, textvariable=self.second_year_2nd_sem, font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_2_2.grid(row=7, column=1, pady=8, padx=20, sticky="ew")
        entry_year_2_2.grid_columnconfigure(0, weight=1)
        #year3
        year_3_1 = Label(Manage_Frame, text="Third_year_1st_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_3_1.grid(row=8, column=0, padx=15, pady=8)
        entry_year_3_1 = Entry(Manage_Frame, textvariable=self.third_year_1st_sem, font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_3_1.grid(row=8, column=1, pady=8, padx=20, sticky="ew")
        entry_year_3_1.grid_columnconfigure(0, weight=1)

        year_3_2 = Label(Manage_Frame, text="Third_year_2nd_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_3_2.grid(row=9, column=0, padx=15, pady=8)
        entry_year_3_2 = Entry(Manage_Frame, textvariable=self.third_year_2nd_sem, font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_3_2.grid(row=9, column=1, pady=8, padx=20, sticky="ew")
        entry_year_3_2.grid_columnconfigure(0, weight=1)
        #year4
        year_4_1 = Label(Manage_Frame, text="Fourth_year_1st_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_4_1.grid(row=10, column=0, padx=15, pady=8)
        entry_year_4_1 = Entry(Manage_Frame, textvariable=self.fourth_year_1st_sem, font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_4_1.grid(row=10, column=1, pady=8, padx=20, sticky="ew")
        entry_year_4_1.grid_columnconfigure(0, weight=1)

        year_4_2 = Label(Manage_Frame, text="Fourth_year_2nd_sem", bg="blue", fg="white",
                         font=('times new roman', 15, "bold"))
        year_4_2.grid(row=11, column=0, padx=15, pady=8)
        entry_year_4_2 = Entry(Manage_Frame, textvariable=self.fourth_year_2nd_sem,
                               font=('times new roman', 10, "bold"),
                               bd=2,
                               relief=GROOVE, width=45)
        entry_year_4_2.grid(row=11, column=1, pady=8, padx=20, sticky="ew")
        entry_year_4_2.grid_columnconfigure(0, weight=1)
        #button
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="navy")
        btn_Frame.place(x=-10, y=545, width=510,height=530)

        addbutton = Button(btn_Frame, text="ADD",font=('arial',10), width=7,height=1, command=self.add_students1, bg="blue", fg="white")
        addbutton.grid(padx=380, pady=10)
        updatebtn = Button(btn_Frame, text="Update",font=('arial',10), width=7,height=1, command=self.update_data, bg="blue", fg="white")
        updatebtn.grid(padx=200,pady=10)
        Clearbtn = Button(btn_Frame, text="Clear",font=('arial',10), width=7,height=1, command=self.clear, bg="blue", fg="white")
        Clearbtn.grid(padx=50,pady=10)
        # detail frame
        Detail_Frame = Frame(self.root, bd=8, relief="sunken", bg="navy")
        Detail_Frame.place(x=510, y=69, width=1050, height=750)

        lbl_Search = Label(Detail_Frame, text="Search By", bg="navy", fg="white",
                           font=('times new roman', 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=25, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10,
                                    font=('Arial', 12), state="readonly")
        combo_search["values"] = ("Registration", "Contact", "s_name")
        combo_search.grid(row=0, column=1, padx=30, pady=10)

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,column=3,padx=18,pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0,column=4,padx=18,pady=10)
        deleteallbtn = Button(Detail_Frame, text="Clear All", width=10, pady=5, command=self.clear_data).grid(row=0,
                                                                                                           column=5,
                                                                                                           padx=18,
                                                                                                           pady=10)

        txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=('times new roman', 10, "bold"),
                           bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=28, sticky="ew")
        #table
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=15, y=100, width=979, height=590)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=(
            "roll", "name", "dept", "contact", "iyi-bl", "iyii-bl", "iiyi-bl", "iiyii-bl", "iiiyi-bl", "iiiyii-bl",
            "ivyi-bl", "ivyii-bl"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="roll_no")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("dept", text="Depart")
        self.Student_table.heading("contact", text="contact")
        self.Student_table.heading("iyi-bl", text="iyi-bl")
        self.Student_table.heading("iyii-bl", text="iyii-bl")
        self.Student_table.heading("iiyi-bl", text="iiyi-bl")
        self.Student_table.heading("iiyii-bl", text="iiyii-bl")
        self.Student_table.heading("iiiyi-bl", text="iiiyi-bl")
        self.Student_table.heading("iiiyii-bl", text="iiiyii-bl")
        self.Student_table.heading("ivyi-bl", text="ivyi-bl")
        self.Student_table.heading("ivyii-bl", text="ivyii-bl")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=60)
        self.Student_table.column("name", width=60)
        self.Student_table.column("dept", width=60)
        self.Student_table.column("contact", width=60)
        self.Student_table.column("iyi-bl", width=60)
        self.Student_table.column("iyii-bl", width=60)
        self.Student_table.column("iiyi-bl", width=60)
        self.Student_table.column("iiyii-bl", width=60)
        self.Student_table.column("iiiyi-bl", width=60)
        self.Student_table.column("iiiyii-bl", width=60)
        self.Student_table.column("ivyi-bl", width=60)
        self.Student_table.column("ivyii-bl", width=60)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

        # self.fetch_data()


    def add_students1(self):
            if self.registration.get() == "" or self.name.get() == "":
                messagebox.showerror("Error", "All fields are required !!!")
            else:
                connection_with_database = connector.connect(host="localhost",
                                                             user="root",
                                                             password="Divij@2005",
                                              database="CMREC_BLOGS")
                cursor = connection_with_database.cursor()
                cursor.execute("insert into students_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.registration.get(),
                             self.name.get(),
                             self.contact.get(),
                             self.branch.get(),
                             self.first_year_1st_sem.get(),
                             self.first_year_2nd_sem.get(),
                             self.second_year_1st_sem.get(),
                             self.second_year_2nd_sem.get(),
                             self.third_year_1st_sem.get(),
                             self.third_year_2nd_sem.get(),
                             self.fourth_year_1st_sem.get(),
                             self.fourth_year_2nd_sem.get()
                             ))
                connection_with_database.commit()
                # self.fetch_data()
                self.clear()
                connection_with_database.close()
                messagebox.showinfo("Success", "Records has been inserted !!!")
    def clear_data(self):
        self.registration.set("")
        self.branch.set("")
        self.name.set("")
        self.contact.set("")
        self.first_year_1st_sem.set("")
        self.first_year_2nd_sem.set("")
        self.second_year_1st_sem.set("")
        self.second_year_2nd_sem.set("")
        self.third_year_1st_sem.set("")
        self.third_year_2nd_sem.set("")
        self.fourth_year_1st_sem.set("")
        self.fourth_year_2nd_sem.set("")
    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        print(row)
        self.registration.set(row[0])
        self.name.set(row[1])
        self.branch.set(row[2])
        self.contact.set(row[3])
        self.first_year_1st_sem.set(row[4])
        self.first_year_2nd_sem.set(row[5])
        self.second_year_1st_sem.set(row[6])
        self.second_year_2nd_sem.set(row[7])
        self.third_year_1st_sem.set(row[8])
        self.third_year_2nd_sem.set(row[9])
        self.fourth_year_1st_sem.set(row[10])
        self.fourth_year_2nd_sem.set(row[11])
    def fetch_data(self):
        con = connector.connect(host="localhost", user="root", password="Divij@2005", database="cmrec_blogs")
        cur = con.cursor()
        cur.execute("select *from students_info")
        rows = cur.fetchall()
        if rows != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END, values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Student_table.delete(*self.Student_table.get_children())
    def delete_data(self):
        con = connector.connect(host="localhost", user="root", password="Divij@2005", database="cmrec_blogs")
        cur = con.cursor()
        # cur.execute("delete from students_info where SROLLNO=%s",self.Roll_No_var.get())
        # cur.execute("delete from students_info where SNAME=%s",self.name_var.get())
        # sql2 = "DELETE FROM students_info WHERE SROLLNO LIKE ?"
        # cur.execute(sql2, (self.Roll_No_var.get()))
        cur.execute("delete from students_info where srollno=%s", self.registration.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        print("ur record has been deleted successfully")

    def search_data(self):
        con = connector.connect(host="localhost", user="root", password="Divij@2005", database="cmrec_blogs")
        cur = con.cursor()
        cur.execute("select * from students_info where " + str(self.search_by.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def update_data(self):
        con = connector.connect(host="localhost", user="root", password="Divij@2005", database="cmrec_blogs")
        cur = con.cursor()
        cur.execute("update students_info set contact=%s where srollno=%s",
                    (self.contact.get(), self.registration.get()))
        con.commit()
        # self.fetch_data()
        self.clear()
        messagebox.showinfo("Contact is updated successfully")
        con.close()







root = Tk()
Student(root)
root.mainloop()
