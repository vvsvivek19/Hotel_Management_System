from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title('Register')
        self.root.geometry("1600x900+0+0")
        self.root.state('zoomed')
 
        #-------------background of register window---------------------
        self.bg = ImageTk.PhotoImage(file=r"D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Register_background.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #------------Main Registration Frame----------------------------

if __name__ == '__main__':
    win = Tk()
    app = Register(win)
    win.mainloop()
