from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random

class Room_Booking:
    def __init__(self,root):
        self.root = root
        self.root.title('Room Booking')
        self.root.geometry('1275x610+250+170')

        #-----------------Variables------------------------------------------------------
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        #---------------------------Title--------------------------------------------
        lbl_title = Label(self.root,text='ROOM BOOKING',font=('Sans',15,'bold'),bg='#0d3b69',fg='white',bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,relwidth=1,height=40)
        
        #---------------------------Hotel Logo---------------------------------------
        img2 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Logo.png')
        img2 = img2.resize((40,40),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
    
        lbl_img2 = Label(self.root, image=self.photoimage2,bd=3,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=40,height=40)

        #----------------------------Label Frame Left---------------------------------
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking Details',padx=2,font=('Segoe UI,',15,'bold'))
        labelframeleft.place(x=5,y=40,width=420,height=565)

        #----------------------------Enteries in Left---------------------------------
        #Cust Contact
        lbl_contact = Label(labelframeleft,text='Customer Contact: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_contact.grid(row=0,column=0,sticky=W)
        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=('Segoe UI,',12,'bold'))
        entry_contact.grid(row=0,column=1,sticky=W)

        #Fetch Data Button 
        btnButtonFetchData = Button(labelframeleft,command=self.fetch_contact,text='Fetch Data',width=8,font=('Segoe UI,',8,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnButtonFetchData.place(x=348,y=4)

        #Check-in Date
        lbl_check_in_date = Label(labelframeleft,text='Check-in Date: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_check_in_date.grid(row=1,column=0,sticky=W)
        txt_check_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=28,font=('Segoe UI,',12,'bold'))
        txt_check_in_date.grid(row=1,column=1)

        #Check-out Date
        lbl_check_out_date = Label(labelframeleft,text='Check-out Date: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)
        txt_check_out_date = ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=28,font=('Segoe UI,',12,'bold'))
        txt_check_out_date.grid(row=2,column=1)

        #Room Type
        label_RoomType = Label(labelframeleft,text="Room Type: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,width=26,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_RoomType['value'] = ("Select","Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1,sticky=W)

        #Available Room
        lbl_Available_Room = Label(labelframeleft,text='Room No: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_Available_Room.grid(row=4,column=0,sticky=W)
        txt_Available_Room = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=28,font=('Segoe UI,',12,'bold'))
        txt_Available_Room.grid(row=4,column=1)

        #Meal
        lbl_Meal = Label(labelframeleft,text='Meal: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0,sticky=W)
        txt_Meal = ttk.Entry(labelframeleft,textvariable=self.var_meal,width=28,font=('Segoe UI,',12,'bold'))
        txt_Meal.grid(row=5,column=1)

        #No. of Days
        lbl_NoOfDays = Label(labelframeleft,text='No. of Days: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_NoOfDays.grid(row=6,column=0,sticky=W)
        txt_NoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=28,font=('Segoe UI,',12,'bold'))
        txt_NoOfDays.grid(row=6,column=1)

        #Paid Tax
        lbl_PaidTaxes = Label(labelframeleft,text='Paid Tax: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_PaidTaxes.grid(row=7,column=0,sticky=W)
        txt_PaidTaxes = ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=28,font=('Segoe UI,',12,'bold'))
        txt_PaidTaxes.grid(row=7,column=1)

        #Sub Total
        lbl_SubTotal = Label(labelframeleft,text='Sub Total: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_SubTotal.grid(row=8,column=0,sticky=W)
        txt_SubTotal = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=28,font=('Segoe UI,',12,'bold'))
        txt_SubTotal.grid(row=8,column=1)

        #Total Cost
        lbl_TotalCost = Label(labelframeleft,text='Total Cost: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_TotalCost.grid(row=9,column=0,sticky=W)
        txt_TotalCost = ttk.Entry(labelframeleft,textvariable=self.var_total,width=28,font=('Segoe UI,',12,'bold'))
        txt_TotalCost.grid(row=9,column=1)

        #----------------------------Buttons in Left---------------------------------
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=360,width=400,height=150)

        #Bill Button
        btnBill = Button(btn_frame,text='Bill',width=38, height=1,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnBill.grid(row=0,column=0,columnspan=2,padx=4,pady=7)

        btnAdd = Button(btn_frame,text='Bill',width=38, height=1,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=0,columnspan=2,padx=4,pady=7)
        
        btnAdd = Button(btn_frame,command=self.add_data,text='Add',width=18, height=1,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.update_data,text='Update',width=18, height=1,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=1,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.delete_data,text='Delete',width=18, height=1,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=2,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.reset_data,text='Reset',width=18, height=1,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=2,column=1,padx=4,pady=7)

        #----------------------------Table Frame for Search---------------------------------
        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',padx=4,font=('Segoe UI,',15,'bold'))
        Table_Frame.place(x=430,y=250,width=840,height=350)

        lblSearchBy = Label(Table_Frame,text="Search Customer ",font=('Segoe UI,',12,'bold'),background='green',fg='white')
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame,width=20,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_Search['value'] = ("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=3)

        self.text_search = StringVar()    
        txtSearch = ttk.Entry(Table_Frame,width=28,font=('Segoe UI,',12,'bold'))
        txtSearch.grid(row=0,column=2,padx=3)

        btnSearch = Button(Table_Frame,text='Search',width=13,font=('Segoe UI,',8,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnSearch.grid(row=0,column=4,padx=3)

        btnShowAll = Button(Table_Frame,text='Show All',width=13,font=('Segoe UI,',8,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnShowAll.grid(row=0,column=5,padx=3)

        #----------------------------Show data table---------------------------------
        details_Table = Frame(Table_Frame,bd=2,relief=RIDGE,padx=4)
        details_Table.place(x=0,y=40,width=840,height=280)
        scroll_x = ttk.Scrollbar(details_Table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_Table,orient=VERTICAL)

        self.room_table = ttk.Treeview(details_Table,column=("contact","checkin","checkout","roomtype","roomavailable","meal"
                                                            ,"noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact No")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room no")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No. of Days")

        self.room_table["show"] = "headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)


        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #--------------------------Button Functionality----------------------------------------------
    def add_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror('Input Error', 'Please Enter Mobile Number',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO roombooking VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()))
                conn.commit()
                # self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Your Room is Booked',parent=self.root)
            except Exception as m:
                messagebox.showwarning('Warning',f'Something went wrong: {m}',parent=self.root)
    
    def fetch_data(self):    
        conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from roombooking")
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

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
    
    def update_data(self):
        if self.var_contact.get() == '':
            messagebox.showerror('Error', 'Pleae Enter Mobile Number',parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE roombooking SET Checkin=%s,Checkout=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,NoOfDays=%s where Mobile=%s',(
                    
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update Successful','Customer Booking Details Updated Successfully',parent=self.root)
        
    def delete_data(self):
        confirm_message = messagebox.askyesno("HMS","Do you really want to delete this booking?",parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM roombooking WHERE Mobile=%s",(self.var_contact.get(),))
        else:
            if not confirm_message:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    
    
    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("Select")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")

    #--------------------------Fetching data frame----------------------------------------------
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror('Error','Please Enter Contact Number!',parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Name FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
            rows = my_cursor.fetchone()

            if rows == None:
                messagebox.showerror('Error',"This number doesn't Exist!")
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root,bd=3,relief=RIDGE,padx=2)
                showDataFrame.place(x=430,y=50,width=840,height=190)

                #----------------------------Name-----------------------------------
                lblName = Label(showDataFrame,text="Name: ",font=('Segoe UI,',12,'bold'))
                lblName.grid(row=0,column=0,sticky=W)

                lblName_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblName_Data.grid(row=0,column=1)

                #----------------------------Gender-----------------------------------
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Gender FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
                rows = my_cursor.fetchone()

                lblGender = Label(showDataFrame,text="Gender: ",font=('Segoe UI,',12,'bold'))
                lblGender.grid(row=1,column=0,sticky=W)

                lblGender_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblGender_Data.grid(row=1,column=1)

                #----------------------------Email-----------------------------------
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Email FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
                rows = my_cursor.fetchone()

                lblGender = Label(showDataFrame,text="Email: ",font=('Segoe UI,',12,'bold'))
                lblGender.grid(row=2,column=0,sticky=W)

                lblEmail_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblEmail_Data.grid(row=2,column=1)

                #----------------------------Nationality-----------------------------------
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Nationality FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
                rows = my_cursor.fetchone()

                lblNationality = Label(showDataFrame,text="Nationality: ",font=('Segoe UI,',12,'bold'))
                lblNationality.grid(row=3,column=0,sticky=W)

                lblNationality_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblNationality_Data.grid(row=3,column=1)

                #----------------------------Address-----------------------------------
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Address FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
                rows = my_cursor.fetchone()

                lblAddress = Label(showDataFrame,text="Address: ",font=('Segoe UI,',12,'bold'))
                lblAddress.grid(row=4,column=0,sticky=W)

                lblAddress_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblAddress_Data.grid(row=4,column=1)

                #----------------------------PostCode-----------------------------------
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT PostCode FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
                rows = my_cursor.fetchone()

                lblPostCode = Label(showDataFrame,text="PostCode: ",font=('Segoe UI,',12,'bold'))
                lblPostCode.grid(row=5,column=0,sticky=W)

                lblPostCode_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblPostCode_Data.grid(row=5,column=1)

                #----------------------------Idproof-----------------------------------
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Idproof FROM customer WHERE Mobile = %s",(self.var_contact.get(),))
                rows = my_cursor.fetchone()

                lblIdproof = Label(showDataFrame,text="Idproof: ",font=('Segoe UI,',12,'bold'))
                lblIdproof.grid(row=6,column=0,sticky=W)

                lblIdproof_Data = Label(showDataFrame,text=rows,font=('Segoe UI,',12,'bold'))
                lblIdproof_Data.grid(row=6,column=1)


if __name__ == '__main__':
    win = Tk()
    app = Room_Booking(win)
    win.mainloop()

