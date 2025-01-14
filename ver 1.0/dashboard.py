from tkinter import*
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Inventory Management System | Developed by Aswin Vibushan")

root=Tk()
obj=IMS(root)
root.mainloop()