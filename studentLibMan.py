import tkinter as Tk
from tkinter import Button, Entry, Frame, Label, Scrollbar, StringVar, font
from tkinter.constants import BOTH, BOTTOM, CHECKBUTTON, END, GROOVE, HORIZONTAL, RIDGE, RIGHT, SUNKEN, TOP, VERTICAL, X
from typing import Text
from tkinter import ttk
from tkinter import Text
import mysql.connector
import requests
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System") #Name of the database or title of database
        self.root.geometry("1350x700+0+0")   #Size of the sheet


        '''------------------------ All variables -----------------------------------------------'''
        self.Roll_no_var=StringVar()
        self.Name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.Address_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
        #After created a page 
        title=Tk.Label(self.root,text="Student Managment System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="DeepSky blue")
        title.pack(side=TOP,fill=X) #fill=X means the length will be extended end to end in page

        #the two frames that we have created in left most part and right most part

        '''------------Manage_Frame---------------'''
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        Manage_Frame.place(x=20,y=70,width=350,height=560)
        m_title=Label(Manage_Frame,text="Manage Student",bd=5,relief=SUNKEN,font=("times new roman",20,"bold"),bg="DeepSky blue3",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        '''--------------------For label of Roll number----------------------------------'''
        lbl_roll=Label(Manage_Frame,text="Roll Number",font=("times new roman",10,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")


        '''--------------------For text Entry of Roll number----------------------------------'''
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_no_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,padx=20,pady=10)

        '''--------------------For label of name----------------------------------'''
        lbl_name=Label(Manage_Frame,text="Name",font=("times new roman",10,"bold"),bd=5)
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        '''--------------------For text Entry of name-------------------------------------------'''
        txt_Name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,padx=20,pady=10)

    
        '''--------------------For label of Email----------------------------------'''
        lbl_email=Label(Manage_Frame,text="Email-id",font=("times new roman",10,"bold"),bd=5)
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        '''--------------------For text Entry of email-------------------------------------------'''
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,padx=20,pady=10)

        
        '''--------------------For label of Gender----------------------------------'''
        lbl_Gender=Label(Manage_Frame,text="Gender",font=("times new roman",10,"bold"),bd=5)
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        '''--------------------For selecting Entry of Gender-------------------------------------------'''
        ccmbo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",10,"bold"),state="readonly")
        ccmbo_gender['values']=("Male","Female","Other")
        ccmbo_gender.grid(row=4,column=1,padx=20,pady=10)

        '''--------------------For label of Contact----------------------------------'''
        lbl_contact=Label(Manage_Frame,text="Contact",font=("times new roman",10,"bold"),bd=5)
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        '''--------------------For text Entry of Contact-------------------------------------------'''
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,padx=20,pady=10)

        
        '''--------------------For label of DOB----------------------------------'''
        lbl_name=Label(Manage_Frame,text="DOB",font=("times new roman",10,"bold"),bd=5)
        lbl_name.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        '''--------------------For text Entry of DOB-------------------------------------------'''
        txt_Name=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=6,column=1,padx=20,pady=10)

        '''--------------------For label of Adderess----------------------------------'''
        lbl_address=Label(Manage_Frame,text="Address",font=("times new roman",10,"bold"),bd=5)
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        
        '''--------------------For  Entrying of Address-------------------------------------------'''
        self.txt_Address=Text(Manage_Frame,width=25,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,padx=20,pady=10,sticky="w")


        #---------------------------------BUTTON-------------------------------------------
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="lightblue")
        btn_Frame.place(x=10,y=480,width=320,height=50)

        Add_button=Button(btn_Frame,text="Add",width=5,command=self.add_students).grid(row=0,column=0,padx=15,pady=10)
        Update_button=Button(btn_Frame,text="Update",width=5,command=self.update_data).grid(row=0,column=1,padx=15,pady=10)
        Delete_button=Button(btn_Frame,text="Delete",width=5,command=self.delete_data).grid(row=0,column=2,padx=15,pady=10)
        clear_button=Button(btn_Frame,text="Clear",width=5,command=self.clear).grid(row=0,column=3,padx=15,pady=10)


        '''------------------------------------Detail Frame------------------------------------'''

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        Detail_Frame.place(x=500,y=70,width=750,height=560)

        lbl_search=Label(Detail_Frame,text="Search By",font=("times new roman",20,"bold"),bd=5)
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",10,"bold"),state='readonly')
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=10,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        search_btn=Button(Detail_Frame,command=self.search_data,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(Detail_Frame,command=self.fetch_data,text="Show All",width=10).grid(row=0,column=4,padx=10,pady=10)

        Tabel_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="lightblue")
        Tabel_Frame.place(x=20,y=70,width=700,height=470)

        scroll_x=Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Tabel_Frame,orient=VERTICAL)
       
        self.Student_table=ttk.Treeview(Tabel_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=X)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll NO")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email-id")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact No")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']="headings"
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_students(self):
        if self.Roll_no_var.get()=="" or self.Name_var.get()=="" or self.email_var.get()=="":
            messagebox.showerror("Error Occured","All fields are required")
        else:    
        #host will define where our host is available  database means database name
            con=mysql.connector.connect(host="localhost" ,user="root" ,passwd="1234" ,database="stm" ,auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
                                                                            self.Name_var.get(),  
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_Address.get('1.0',END)
                                                                            ))    
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Successfully ","Record has been inserted")
    
    
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="stm",auth_plugin='mysql_native_password')
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            #deleting data from the table
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.Roll_no_var.set("")
        self.Name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)


    #to get data when clicked on particular value
    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_no_var.set(row[0])
        self.Name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="stm",auth_plugin='mysql_native_password')
        cur = con.cursor()
        cur.execute("update  students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                         self.Name_var.get(),  
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END),
                                                                         self.Roll_no_var.get()
                                                                         ))    
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="stm",auth_plugin='mysql_native_password')
        cur = con.cursor()
        print(self)
        cur.execute("DELETE FROM students WHERE roll_no=" + (self.Roll_no_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()    
            
    def search_data(self):
        if self.search_by.get()=="":
            messagebox.showerror("Error","Please write something")
        
        else:
            con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="stm",auth_plugin='mysql_native_password')
            cur = con.cursor()
            cur.execute("select * from students where "+ self.search_by.get() +" LIKE '%"+ self.search_txt.get() +"'") 
            rows = cur.fetchall()
            print(rows)
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()
        
            
   

root = Tk.Tk()
ob=Student(root)
root.mainloop()        
