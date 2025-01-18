from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by 6cyn")
        self.root.config(bg="white")
        self.root.focus_force()

        #====SearchFrame====
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options======
        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Employee ID","Phone No","Name"),state="readonly",justify=CENTER)
        cmb_search.place(x=10,y=10,width=180)







if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()