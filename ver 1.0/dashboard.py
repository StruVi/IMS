from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | Developed by 6cyn")
        self.root.config(bg="white")

        #====title====
        self.icon_title=PhotoImage(file="images/carts.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx="20").place(x=0,y=0,relwidth=1,height=70)

        #====btn_logout====
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1720,y=10,height=50,width=150)

        #====Clock====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Menu=====
        self.Menu_icon=Image.open("images\IM-menu.png")
        self.Menu_icon=self.Menu_icon.resize((200,200))  
        self.Menu_icon=ImageTk.PhotoImage(self.Menu_icon)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_MenuIcon=Label(LeftMenu,image=self.Menu_icon)
        lbl_MenuIcon.pack(side=TOP,fill=X)

        self.icon1=PhotoImage(file="images/menu icons/employee.png")
        self.icon2=PhotoImage(file="images/menu icons/supplier.png")
        self.icon3=PhotoImage(file="images/menu icons/category.png")
        self.icon4=PhotoImage(file="images/menu icons/product.png")
        self.icon5=PhotoImage(file="images/menu icons/sale.png")
        self.icon6=PhotoImage(file="images/menu icons/exit.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Employee",image=self.icon1,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",image=self.icon2,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",image=self.icon3,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Products",image=self.icon4,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon5,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon6,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Content====
        self.lbl_employee=Label(self.root,text="Total Employees\n[0]",bg="#33bbf9",fg="white",bd=5,relief=RIDGE,font=("goudy old style",20,"bold")).place(x=300,y=120,width=300,height=150)



        #====Footer====
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed by 6cyn\nFor any Technical Issues Contact: 9790326149",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

root=Tk()
obj=IMS(root)
root.mainloop()