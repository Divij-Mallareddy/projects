import tkinter as tk
from tkinter import *
import pymongo
from tkinter import messagebox


class student:
    def __init__(self,window):
        self.window = window
        window.geometry("1600x900")
        window.title("STUDENT MANAGEMENT SYSTEM")
        self.sid = StringVar()
        self.sname = StringVar()
        self.scontact =StringVar()

        f1 = Frame(window,bg="coral",bd=6,relief="flat")
        f1.place(x=260,y=98,width=1000,height=600)
        # Configure grid for centering
        f1.grid_rowconfigure(0, weight=1)
        f1.grid_rowconfigure(1, weight=0)
        f1.grid_rowconfigure(2, weight=0)
        f1.grid_rowconfigure(3, weight=0)
        f1.grid_rowconfigure(4, weight=0)
        f1.grid_rowconfigure(5, weight=0)
        f1.grid_rowconfigure(6, weight=1)
        f1.grid_rowconfigure(99, weight=2)
        f1.grid_columnconfigure(0, weight=1)
        f1.grid_columnconfigure(1, weight=0)
        f1.grid_columnconfigure(2, weight=0)
        f1.grid_columnconfigure(3, weight=0)
        f1.grid_columnconfigure(4, weight=0)
        f1.grid_columnconfigure(5,weight=1)

        # Label
        l1 = Label(f1, text="STUDENT ID", bg="white", bd=6, font=("Courier", 14))
        l1.grid(row=0, column=1, padx=10, pady=10, sticky="se")

        # Entry
        e1 = Entry(f1, textvariable=self.sid, font=("Courier", 14))
        e1.grid(row=0, column=2, padx=10, pady=10, sticky="sw")

        l2 = Label(f1, text="STUDENT NAME", bg="white", bd=6, font=("Courier", 14))
        l2.grid(row=1, column=1, padx=10, pady=10, sticky="se")

        # Entry
        e2 = Entry(f1, textvariable=self.sname, font=("Courier", 14))
        e2.grid(row=1, column=2, padx=10, pady=10, sticky="nw")

        l3 = Label(f1, text="STUDENT CONTACT", bg="white", bd=6, font=("Courier", 14))
        l3.grid(row=2, column=1, padx=10, pady=10, sticky="ne")

        # Entry
        e3 = Entry(f1, textvariable=self.scontact, font=("Courier", 14))
        e3.grid(row=2, column=2, padx=10, pady=10, sticky="nw")

        #button
        b1 = Button(f1, text="Enroll",font=6, command=self.enroll)
        b1.grid(row=6, column=2,sticky="e",padx=10,pady=20)
        b2 = Button(f1, text="Update",font=6, command=self.update)
        b2.grid(row=6, column=3,sticky="w",padx=10,pady=20)
        b3 = Button(f1, text="Show Data",font=6, command=self.show_all)
        b3.grid(row=6, column=4,sticky="e",padx=10,pady=20)

        #diaplay
        self.display = Text(f1, font=("Courier", 18), height=4, width=50, state="disabled")
        self.display.grid(row=7, column=0, columnspan=4, padx=20, pady=20)

    def mongodb(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["STUDENT_DATABASE"]
        collection = db["STUDENT_DATA"]
        return client,db,collection


        #functions
    def enroll(self):
        if self.sid.get() == "" or self.sname.get() == "" or self.scontact.get() == "":
            messagebox.showerror("ERROR","PLEASE ENTER ALL THE DATA")
        else:
            client,db,collection = self.mongodb()
            a = {"Student_id":self.sid.get(),"Student_name":self.sname.get(),"Student_contact":self.scontact.get()}
            x = collection.insert_one(a)
            self.clear()
            messagebox.showinfo("SUCCESS","Data is 'inserted' successfully.")

    def update(self):
        if self.sid.get() == "":
            messagebox.showerror("ERROR","please enter 'ID' you want to change.")


        client, db, collection = self.mongodb()

        a = {"Student_id": self.sid.get()}
        update_dict = {}
        if self.sname.get() != "":
            update_dict["Student_name"] = self.sname.get()
        if self.scontact.get() != "":
            update_dict["Student_contact"] = self.scontact.get()
        if not update_dict:
            messagebox.showerror("ERROR", "Please enter data to update.")
            return

        # Perform the update
        b = {"$set": update_dict}
        collection.update_one(a, b)
        self.clear()
        messagebox.showinfo("SUCCESS", "Data has been entered successfully")

    def show_all(self):
        self.display.config(state="normal")
        self.display.delete("1.0", tk.END)

        # Connect to MongoDB
        client, db, collection = self.mongodb()


        uid = {"Student_id": self.sid.get()}


        cursor = collection.find(uid, {"_id": 0, "Student_name": 1, "Student_contact": 1})


        student_info = ""
        for document in cursor:
            student_info += f"Name: {document['Student_name']}, Phone: {document['Student_contact']}\n"


        if student_info:
            self.display.insert(tk.END, student_info)
        else:
            self.display.insert(tk.END, "No data found for this Student ID.")

        self.display.config(state="disabled")

    def clear(self):
        self.sid.set("")
        self.sname.set("")
        self.scontact.set("")



window = Tk()
student(window)
window.mainloop()