from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | Developed by Aswin Vibushan")
        self.root.config(bg="white")

        #====title====
        self.icon_title=PhotoImage(file="images/carts.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx="20").place(x=0,y=0,relwidth=1,height=70)

        #====btn_logout====
        btm_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1720,y=10,height=50,width=150)

        #====Clock====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Menu=====
        self.Menu_icon=Image.open("images\IM-menu.png")
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=700)


root=Tk()
obj=IMS(root)
root.mainloop()