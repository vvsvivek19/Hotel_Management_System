from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title('Hospital Management System')
        self.root.geometry('1550x800+0+0')
        self.root.state('zoomed')
        
        #----------------First Image - Hotel Managment System----------------------------

        img1 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Background.png')
        img1 = img1.resize((1550,140),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lbl_img = Label(self.root, image=self.photoimage1,bd=4,relief=RIDGE)
        lbl_img.place(x=0,y=0,width=1600,height=140)

        #----------------Hotel Logo------------------------------------------

        img2 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Logo.png')
        img2 = img2.resize((200,140),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        
        lbl_img2 = Label(self.root, image=self.photoimage2,bd=4,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=200,height=140)

        #-------------------Main Frame-----------------------------------------
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=140,width=1550,height=660)

if __name__ == '__main__':
    win = Tk()
    app = HotelManagementSystem(win)
    win.mainloop()