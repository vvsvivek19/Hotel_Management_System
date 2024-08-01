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

        #-----------------Variables------------------------------------------------------
        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.var_roomtype = StringVar()

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
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor,width=30,font=('Segoe UI,',12,'bold'))
        entry_floor.grid(row=0,column=1)

        #Room Number
        lbl_RoomNo = Label(labelframeleft,text='Room Number: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=30,font=('Segoe UI,',12,'bold'))
        entry_RoomNo.grid(row=1,column=1)

        #Room Type
        lbl_RoomType = Label(labelframeleft,text='Room Type: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,width=28,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_RoomType['value'] = ("Select","Single","Double","Luxury","Duplex")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=2,column=1)

        #----------------------------Buttons in Left---------------------------------
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=60,y=150,width=480,height=175)

        btnAdd = Button(btn_frame,command=self.add_data,text='Add',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.update_data,text='Update',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=1,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.delete_data,text='Delete',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.reset_data,text='Reset',width=22, height=3,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
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
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
       

        self.room_table["show"] = "headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    #--------------------------Button Functionality----------------------------------------------
    def add_data(self):
        if self.var_floor.get() == "" and self.var_roomtype.get() == '':
            messagebox.showerror('Input Error', 'Please Floor Number and Room Type',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO room_management VALUES (%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_roomtype.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','New Room is Added!',parent=self.root)
            except Exception as m:
                messagebox.showwarning('Warning',f'Something went wrong: {m}',parent=self.root)
    
    def fetch_data(self):    
        conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room_management")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

    def update_data(self):
        if self.var_floor.get() == "" and self.var_roomtype.get() == '':
            messagebox.showerror('Input Error', 'Please Floor Number and Room Type',parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE room_management SET Floor=%s,RoomType=%s where RoomNo=%s',(
                    
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update Successful','Room Details Updated Successfully!!!',parent=self.root)
    
    def delete_data(self):
        confirm_message = messagebox.askyesno("HMS","Do you really want to delete this room?",parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM room_management WHERE RoomNo=%s",(self.var_roomno.get(),))
        else:
            if not confirm_message:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    
    
    def reset_data(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("Select")

if __name__ == '__main__':
    win = Tk()
    app = Room_Management(win)
    win.mainloop()
