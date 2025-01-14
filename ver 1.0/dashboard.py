from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | Developed by Aswin Vibushan")

        #====title====
        self.icon_title=PhotoImage(file="images/carts.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="green",anchor="w",padx="20").place(x=0,y=0,relwidth=1,height=70)

        #====btn_logout====
        btm_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1720,y=10,height=50,width=150)


root=Tk()
obj=IMS(root)
root.mainloop()