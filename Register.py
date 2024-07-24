from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title('Register')
        self.root.geometry("1600x900+0+0")
        self.root.state('zoomed')

        #--------------Variable Declarions-------------------------------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()
 
        #-------------background of register window---------------------
        self.bg = ImageTk.PhotoImage(file=r"D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Register_background.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #------------Main Registration Frame----------------------------
        frame = Frame(self.root,bg='#e1a363')
        frame.place(relx=0.20,rely=0.15,relwidth=0.60,relheight=0.70)

        #-------------Main Label inside Main Frame----------------------
        register_lbl = Label(frame,text='REGISTER HERE',font=('Google Sans',20,'bold'),bg='#e1a363',fg='darkgreen')
        register_lbl.place(relx=0.38,rely=0.05)

        #-------------Labels and Entry-------------------
        #1st Row
        fname = Label(frame,text='First Name: ',font=('Sans',15,'bold'),bg='#e1a363')
        fname.place(relx=0.15,rely=0.15)
        self.fname_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_fname)
        self.fname_entry.place(relx=0.15,rely=0.22,relwidth=0.30)

        lname = Label(frame,text='Last Name: ',font=('Sans',15,'bold'),bg='#e1a363')
        lname.place(relx=0.55,rely=0.15)
        self.lname_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_lname)
        self.lname_entry.place(relx=0.55,rely=0.22,relwidth=0.30)

        #2nd Row
        contact = Label(frame,text='Contact No: ',font=('Sans',15,'bold'),bg='#e1a363')
        contact.place(relx=0.15,rely=0.29)
        self.contact_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_contact)
        self.contact_entry.place(relx=0.15,rely=0.36,relwidth=0.30)

        email = Label(frame,text='Email ID: ',font=('Sans',15,'bold'),bg='#e1a363')
        email.place(relx=0.55,rely=0.29)
        self.email_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_email)
        self.email_entry.place(relx=0.55,rely=0.36,relwidth=0.30)

        #3rd Row
        security_Q = Label(frame,text='Select Security Question: ',font=('Sans',15,'bold'),bg='#e1a363')
        security_Q.place(relx=0.15,rely=0.43)
        self.combo_security_Q = ttk.Combobox(frame,font=('Sans',15),state="readonly",textvariable=self.var_securityQ)
        self.combo_security_Q["values"] = ("Select", "Your Birthplace","Your Girlfriend's name","Your Pet Name")
        self.combo_security_Q.place(relx=0.15,rely=0.50,relwidth=0.30)
        self.combo_security_Q.current(0)
    

        security_A = Label(frame,text='Security Answer: ',font=('Sans',15,'bold'),bg='#e1a363')
        security_A.place(relx=0.55,rely=0.43)
        self.security_A_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_securityA)
        self.security_A_entry.place(relx=0.55,rely=0.50,relwidth=0.30)

        #4th Row
        password = Label(frame,text='Password: ',font=('Sans',15,'bold'),bg='#e1a363')
        password.place(relx=0.15,rely=0.57)
        self.password_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_pass)
        self.password_entry.place(relx=0.15,rely=0.64,relwidth=0.30)

        password_confirm = Label(frame,text='Confirm Password: ',font=('Sans',15,'bold'),bg='#e1a363')
        password_confirm.place(relx=0.55,rely=0.57)
        self.password_confirm_entry = ttk.Entry(frame,font=('Sans',15),textvariable=self.var_confpass)
        self.password_confirm_entry.place(relx=0.55,rely=0.64,relwidth=0.30)

        #-----------------Checkbutton---------------------------
        checkbtn = Checkbutton(frame,variable=self.var_check, text='I Agree with Terms & Conditions.',font=('Sans',15,'bold'),bg='#e1a363',activebackground='#e1a363',onvalue=1,offvalue=0)
        checkbtn.place(relx=0.15,rely=0.71)

        #------------------Buttons--------------------------------
        b1 = Button(frame,text='Register Now',command=self.register_data,borderwidth=0,font=('Sans',15,'bold'),bg='purple',fg='white',activebackground='purple',activeforeground='white',cursor='hand2')
        b1.place(relx=0.15,rely=0.80,relheight=0.08,relwidth=0.30)

        b2 = Button(frame,text='Login Now',borderwidth=0,font=('Sans',15,'bold'),bg='green',fg='white',activebackground='green',activeforeground='white',cursor='hand2')
        b2.place(relx=0.55,rely=0.80,relheight=0.08,relwidth=0.30)
    
    #-------------------Function Declaration-----------------------------
    #Below function performs some data validation
    def register_data(self):
        if self.var_fname.get() == '' or self.var_email.get() == '' or self.var_securityQ == 'Select':
            messagebox.showerror('Error',"All fields are required!")
        elif self.var_contact.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error',"All fields are required!")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must be Same!")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please Agree our terms and conditions!")
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hospital_management_system')
            my_cursor = conn.cursor()
            #checking whether already exists or not
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'User already exists, Please try another email ID!')
            else:
                #if user doesn't exists then we insert its data in the database.
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securityQ.get(),
                self.var_securityA.get(),
                self.var_pass.get()
                                                                                    ))
                conn.commit()
                conn.close()
                #showing a message once the registration is successful!!!
                messagebox.showinfo("Success","Registration Successful!")
        



if __name__ == '__main__':
    win = Tk()
    app = Register(win)
    win.mainloop()
