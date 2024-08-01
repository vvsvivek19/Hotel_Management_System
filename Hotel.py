from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random

from Customer import *
from Room_Booking import *
from Room_Management import *

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

        lbl_img = Label(self.root, image=self.photoimage1,bd=3,relief=RIDGE)
        lbl_img.place(x=0,y=0,width=1600,height=140)

        #----------------Hotel Logo------------------------------------------

        img2 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Logo.png')
        img2 = img2.resize((200,140),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        
        lbl_img2 = Label(self.root, image=self.photoimage2,bd=3,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=200,height=140)

        #-------------------Main Frame-----------------------------------------
        main_frame = Frame(self.root,bd=3,relief=RIDGE)
        main_frame.place(x=0,y=140,width=1550,height=660)

        #------------------Menu Frame------------------------------------------
        lbl_menu = Label(main_frame,text='MENU',font=('Sans',20,'bold'),bg='#8beb8b',fg='#132131',bd=3,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=250)

        #-------------------Button Frame-----------------------------------------
        btn_frame = Frame(main_frame,bd=3,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=250,height=200)

        cust_btn = Button(btn_frame,command=self.cust_details,width=20,text='REGISTER CUSTOMER',font=('Sans',15,'bold'),bg='#8beb8b',fg='#132131',bd=0,cursor='hand2',activebackground='#8beb8b',activeforeground='#132131')
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,command=self.room_booking,width=20,text='ROOM BOOKING',font=('Sans',15,'bold'),bg='#8beb8b',fg='#132131',bd=0,cursor='hand2',activebackground='#8beb8b',activeforeground='#132131')
        room_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame,command=self.details,width=20,text='MANAGE ROOMS',font=('Sans',15,'bold'),bg='#8beb8b',fg='#132131',bd=0,cursor='hand2',activebackground='#8beb8b',activeforeground='#132131')
        details_btn.grid(row=2,column=0,pady=1)

        report_btn = Button(btn_frame,width=20,text='DEV DETAILS',font=('Sans',15,'bold'),bg='#8beb8b',fg='#132131',bd=0,cursor='hand2',activebackground='#8beb8b',activeforeground='#132131')
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,command=self.logout,width=20,text='LOGOUT',font=('Sans',15,'bold'),bg='#8beb8b',fg='#132131',bd=0,cursor='hand2',activebackground='#8beb8b',activeforeground='#132131')
        logout_btn.grid(row=4,column=0,pady=1)

        #--------------------RIGHT SIDE IMAGE------------------------------------

        img3 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Interior.jpg')
        img3 = img3.resize((1300,660),Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        
        lbl_img3 = Label(main_frame, image=self.photoimage3,bd=3,relief=RIDGE)
        lbl_img3.place(x=250,y=0,width=1300,height=660)

        #--------------------DOWN SIDE IMAGE------------------------------------

        img4 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Food1.png')
        img4 = img4.resize((700,200),Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        
        lbl_img4 = Label(main_frame, image=self.photoimage4,bd=3,relief=RIDGE)
        lbl_img4.place(x=0,y=235,width=250,height=200)

        img5 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Food2.png')
        img5 = img5.resize((500,250),Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        
        lbl_img5 = Label(main_frame, image=self.photoimage5,bd=3,relief=RIDGE)
        lbl_img5.place(x=0,y=430,width=250,height=240)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)
    
    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Booking(self.new_window)
    
    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Management(self.new_window)

    def logout(self):
        self.root.destroy()
if __name__ == '__main__':
    win = Tk()
    app = HotelManagementSystem(win)
    win.mainloop()