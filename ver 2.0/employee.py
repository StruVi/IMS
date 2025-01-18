from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | Developed by 6cyn")
        self.root.config(bg="white")


if __name__=="__main__":
root=Tk()
obj=employeeClass(root)
root.mainloop()