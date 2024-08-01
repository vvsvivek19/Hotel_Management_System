from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import datetime

class Room_Management:
    def __init__(self,root):
        self.root = root
        self.root.title('Details')
        self.root.geometry('1275x610+250+170')

        #---------------------------Title--------------------------------------------
        lbl_title = Label(self.root,text='ROOMS MANAGEMENT',font=('Sans',15,'bold'),bg='#0d3b69',fg='white',bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,relwidth=1,height=40)
        
        #---------------------------Hotel Logo---------------------------------------
        img2 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Logo.png')
        img2 = img2.resize((40,40),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
    
        lbl_img2 = Label(self.root, image=self.photoimage2,bd=3,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=40,height=40)

        #----------------------------Label Frame Left---------------------------------
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Add New Rooms',padx=2,font=('Segoe UI,',15,'bold'))
        labelframeleft.place(x=5,y=40,width=600,height=450)

        #----------------------------Enteries in Left---------------------------------
        #Floor
        lbl_floor = Label(labelframeleft,text='Floor: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        entry_floor = ttk.Entry(labelframeleft,width=30,font=('Segoe UI,',12,'bold'))
        entry_floor.grid(row=0,column=1)

        #Floor
        lbl_RoomNo = Label(labelframeleft,text='Room Number: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        entry_RoomNo = ttk.Entry(labelframeleft,width=30,font=('Segoe UI,',12,'bold'))
        entry_RoomNo.grid(row=1,column=1)

        #Floor
        lbl_RoomType = Label(labelframeleft,text='Room Type: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        entry_RoomType = ttk.Entry(labelframeleft,width=30,font=('Segoe UI,',12,'bold'))
        entry_RoomType.grid(row=2,column=1)

        #----------------------------Buttons in Left---------------------------------
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=60,y=150,width=480,height=175)

        btnAdd = Button(btn_frame,text='Add',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,text='Update',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=1,padx=4,pady=7)

        btnAdd = Button(btn_frame,text='Delete',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,text='Reset',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=1,padx=4,pady=7)

        #----------------------------Table Frame for Show Room---------------------------------
        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',padx=4,font=('Segoe UI,',15,'bold'))
        Table_Frame.place(x=610,y=40,width=660,height=450)
        scroll_x = ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Roomno")
        self.room_table.heading("roomtype",text="Roomtype")
       

        self.room_table["show"] = "headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)

        # self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        # self.fetch_data()

if __name__ == '__main__':
    win = Tk()
    app = Room_Management(win)
    win.mainloop()
