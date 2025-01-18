from tkinter import*
from PIL import Image,ImageTk #pip install pillow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | Developed by 6cyn")
        self.root.config(bg="white")