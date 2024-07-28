from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random

class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title('Customer')
        self.root.geometry('1275x610+250+170')

         #-----------------Variables------------------------------------------------------
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        
        #---------------------------Title--------------------------------------------
        lbl_title = Label(self.root,text='CUTOMER DETAILS',font=('Sans',15,'bold'),bg='#0d3b69',fg='white',bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=0,relwidth=1,height=40)
        
        #---------------------------Hotel Logo---------------------------------------
        img2 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Logo.png')
        img2 = img2.resize((40,40),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
    
        lbl_img2 = Label(self.root, image=self.photoimage2,bd=3,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=40,height=40)

        #----------------------------Label Frame Left---------------------------------
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',padx=2,font=('Segoe UI,',15,'bold'))
        labelframeleft.place(x=5,y=40,width=420,height=565)

        #----------------------------Enteries in Left---------------------------------
        #cust Ref
        lbl_cust_ref = Label(labelframeleft,text='Customer Ref: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width=28,font=('Segoe UI,',12,'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)

        #cust name
        cname = Label(labelframeleft,text='Customer Name: ',font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=28,font=('Segoe UI,',12,'bold'))
        txtcname.grid(row=1,column=1)

        #Mother's name
        mothername = Label(labelframeleft,text="Mother's Name: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        mothername.grid(row=2,column=0,sticky=W)
        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother,width=28,font=('Segoe UI,',12,'bold'))
        txtmname.grid(row=2,column=1)

        #gender combo box
        labelgender = Label(labelframeleft,text="Gender: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        labelgender.grid(row=3,column=0,sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=26,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_gender['value'] = ("Select","Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1,sticky=W)

        #Postcode
        lblpostcode = Label(labelframeleft,text="Post Code: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_post,width=28,font=('Segoe UI,',12,'bold'))
        txtPostCode.grid(row=4,column=1)

        #mobile number
        lblMobile = Label(labelframeleft,text="Mobile No.: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=28,font=('Segoe UI,',12,'bold'))
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail = Label(labelframeleft,text="Email ID: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email,width=28,font=('Segoe UI,',12,'bold'))
        txtEmail.grid(row=6,column=1)

        #Nationality Combox
        labelNationality = Label(labelframeleft,text="Nationality: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        labelNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,width=26,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_Nationality['value'] = ("Select","India","USA","UK","China","Sri Lanka", "Bangladesh","Nepal", "Australia", "New Zealand", "South Africa", "France", "Japan", "Canada", "Brazil" ,"Others")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1,sticky=W)


        #ID Proof Combox
        labelIdProof = Label(labelframeleft,text="ID Proof: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        labelIdProof.grid(row=8,column=0,sticky=W)

        combo_IdProof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,width=26,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_IdProof['value'] = ("Select","Aadhar","VoterID","Driving License","Passport")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8,column=1,sticky=W)

        #ID Number
        lblIdNumber = Label(labelframeleft,text="Id Number: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=28,font=('Segoe UI,',12,'bold'))
        txtIdNumber.grid(row=9,column=1)


        #Address
        lblAddress = Label(labelframeleft,text="Address: ",font=('Segoe UI,',12,'bold'),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_address,width=28,font=('Segoe UI,',12,'bold'))
        txtAddress.grid(row=10,column=1)

        #----------------------------Buttons in Left---------------------------------
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=390,width=400,height=140)

        btnAdd = Button(btn_frame,text='Add',command=self.add_data,width=18, height=2,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.update_data,text='Update',width=18, height=2,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=0,column=1,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.delete_data,text='Delete',width=18, height=2,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=0,padx=4,pady=7)

        btnAdd = Button(btn_frame,command=self.reset_data,text='Reset',width=18, height=2,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnAdd.grid(row=1,column=1,padx=4,pady=7)

        #----------------------------Table Frame for Search---------------------------------
        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details and Search System',padx=4,font=('Segoe UI,',15,'bold'))
        Table_Frame.place(x=430,y=40,width=840,height=565)

        lblSearchBy = Label(Table_Frame,text="Search Customer ",font=('Segoe UI,',12,'bold'),background='green',fg='white')
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var,width=20,font=('Segoe UI,',12,'bold'), state='readonly')
        combo_Search['value'] = ("Mobile","Ref","Email","Name")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=3)

        self.text_search = StringVar()    
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.text_search,width=28,font=('Segoe UI,',12,'bold'))
        txtSearch.grid(row=0,column=2,padx=3)

        btnSearch = Button(Table_Frame,command=self.search_data,text='Search',width=10,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnSearch.grid(row=0,column=4,padx=3)

        btnShowAll = Button(Table_Frame,command=self.fetch_data,text='Show All',width=8,font=('Segoe UI,',12,'bold'),bg='black',fg='gold',activebackground='black',activeforeground='gold')
        btnShowAll.grid(row=0,column=5,padx=3)

        #----------------------------Show data table---------------------------------
        details_Table = Frame(Table_Frame,bd=2,relief=RIDGE,padx=4)
        details_Table.place(x=0,y=40,width=840,height=500)
        scroll_x = ttk.Scrollbar(details_Table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_Table,orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_Table,column=("ref","name","mother","gender","post","mobile"
                                                            ,"email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Customer Name")
        self.Cust_Details_Table.heading("mother",text="Mother's Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile No")
        self.Cust_Details_Table.heading("email",text="Email ID")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    #----------------------------Button Functionality---------------------------------
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_cust_name.get() == '':
            messagebox.showerror('Input Error', 'Please Enter Mobile Number and Name',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Customer is Registered',parent=self.root)
            except Exception as m:
                messagebox.showwarning('Warning',f'Something went wrong: {m}',parent=self.root)

    def fetch_data(self):    
        conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()
        

    def get_cursor(self,event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])
    
    def update_data(self):
        if self.var_mobile.get() == '':
            messagebox.showerror('Error', 'Pleae Enter Mobile Number',parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute('UPDATE customer SET Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s',(
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update Successful','Customer Details Updated Successfully',parent=self.root)

    def delete_data(self):
        confirm_message = messagebox.askyesno("HMS","Do you really want to delete these customer details?",parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM customer WHERE Ref=%s",(self.var_ref.get(),))
        else:
            if not confirm_message:
                return
        conn.commit()
        self.fetch_data()
        conn.close()    

    def reset_data(self):
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("Select")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Select")
        self.var_id_proof.set("Select")
        self.var_id_number.set("")
        self.var_address.set("")

    def search_data(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM customer WHERE ' + str(self.search_var.get()) + "=" + str(self.text_search.get()))
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == '__main__':
    win = Tk()
    app = Cust_Win(win)
    win.mainloop()
