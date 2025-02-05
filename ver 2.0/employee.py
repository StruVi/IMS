from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=======================
        #All Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_eid=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        #====SearchFrame====
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Employee ID","Phone No","Name"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=200,y=10,width=180)

        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2")
        btn_search.place(x=400,y=7,width=180,height=32)


        #====Tileframe====
        title=Label(self.root,text="Employee Details",font=("goudy old style",20),bg="#0f4d7d",fg="white").place(x=0,y=90,width=1100,height=35)

        #====ContentFrame====
        
        #====row1====
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        
        
        txt_empid=Entry(self.root,textvariable=self.var_eid,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

        #====row2====
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)
        
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="white").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #====row3====
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_usertype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
        
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_password=Entry(self.root,textvariable=self.var_password,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_usertype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="white").place(x=850,y=230,width=180)
        cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_usertype.place(x=850,y=230,width=180)
        cmb_usertype.current(0)

        #====row4====
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
        
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
        
        #====ButtonFrame====
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
        #====Employee Table====
        emp_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scroll_x=Scrollbar(emp_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(emp_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(emp_frame,columns=("eid","Name","Email","Gender","Contact","DOB","DOJ","Password","User-type","Address","Salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("eid",text="eid")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("Email",text="Email")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("Contact",text="Contact")
        self.employee_table.heading("DOB",text="DOB")
        self.employee_table.heading("DOJ",text="DOJ")
        self.employee_table.heading("Password",text="Password")
        self.employee_table.heading("User-type",text="User-type")
        self.employee_table.heading("Address",text="Address")
        self.employee_table.heading("Salary",text="Salary")

        self.employee_table["show"]="headings"

        self.employee_table.column("eid",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("Email",width=100)
        self.employee_table.column("Gender",width=100)
        self.employee_table.column("Contact",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("DOJ",width=100)
        self.employee_table.column("Password",width=100)
        self.employee_table.column("User-type",width=100)
        self.employee_table.column("Address",width=100)
        self.employee_table.column("Salary",width=100)
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
              
    #=======================Database Functions=======================
    def add(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()

        # Check if Employee ID already exists
        try:
            if self.var_eid.get()=="":
                messagebox.showerror("Error","Employee ID is required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_eid.get(),))
                row=cur.fetchone()
                # Insert employee data into the database
                if row!=None:
                    messagebox.showerror("Error", "This Employee ID is alreafy assigned, try different a one.",parent=self.root)
                else:
                    cur.execute("""INSERT INTO employee (eid, Name, Email, Gender, Contact, "DOB", "DOJ", Password, Usertype, Address, Salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""),
                (
                    (
                        self.var_eid.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),

                        self.var_dob.get(),
                        self.var_doj.get(),

                        self.var_password.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END),
                        self.var_salary.get(),
                    ),
                )
                con.commit()
                messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                self.show()   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
        
    def show(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows=cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
   
    def get_data(self,ev):
        f=self.employee_table.focus()
        content=(self.employee_table.item(f))
        row=content['values']
        
        #print(row)

        self.var_eid.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_password.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    
    def update(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()

        # Check if Employee ID already exists
        try:
            if self.var_eid.get()=="":
                messagebox.showerror("Error","Employee ID is required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_eid.get(),))
                row=cur.fetchone()
                # Insert employee data into the database
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID",parent=self.root)
                else:
                    cur.execute
                    ("""Update employee set Name=?, Email=?, Gender=?, Contact=?, "DOB"=?, "DOJ"=?, Password=?, Usertype=?, Address=?, Salary=? where eid=?""",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),

                            self.var_dob.get(),
                            self.var_doj.get(),

                            self.var_password.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_eid.get(),
                     
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
       
                
    def delete(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()

        try:
            if self.var_eid.get()=="":
                messagebox.showerror("Error","Employee ID is required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_eid.get(),))
                row=cur.fetchone()
                # Insert employee data into the database
                if row==None:
                    messagebox.showerror("Error", "Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_eid.get(),))
                        con.commit()
                        self.show()
                    else:
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=self.root)
              
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
       



#=========================================================================================================




if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()