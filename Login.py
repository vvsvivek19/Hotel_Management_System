from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title('Login')
        self.root.geometry("1550x800+0+0")
        self.root.state('zoomed')

        #background of login window
        self.bg = ImageTk.PhotoImage(file=r"D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Login_background.png")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        #Creating a frame for login
        frame = Frame(self.root,bg='#e1a363')
        frame.place(relx=0.35,rely=0.20,relheight=0.70,relwidth=0.30)

        #inserting a login logo
        img1 = Image.open(r"D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Login_Logo.png")
        img1 = img1.resize((100,100),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg='#e1a363',borderwidth=0)
        lblimg1.place(relx=0.47,rely=0.22, width=100,height=100)

        #inserting message below the logo for user
        get_str = Label(frame,text='ENTER LOGIN CREDENTIALS',font=('Sans',20,'bold'),fg='black',bg='#e1a363')
        get_str.place(relx=0.08,rely=0.23)

        #username label and Entry
        username = Label(frame,text='Username',font=('Sans',15,'bold'),fg='black',bg='#e1a363')
        username.place(relx=0.38,rely=0.33)
        self.txtuser = ttk.Entry(frame,font=('Sans',15))
        self.txtuser.place(relx=0.20,rely=0.40,relwidth=0.60) 

        #Password Label and Entry
        password = Label(frame,text='Password',font=('Sans',15,'bold'),fg='black',bg='#e1a363')
        password.place(relx=0.38,rely=0.49)
        self.txtpass = ttk.Entry(frame,font=('Sans',15))
        self.txtpass.place(relx=0.20,rely=0.57,relwidth=0.60) 

        #Login Button
        loginbtn = Button(frame, command=self.login, text='Login',font=('Sans',15,'bold'),bd=3,relief=RIDGE,fg='white',bg='#447404',activeforeground='white',activebackground='#447404')
        loginbtn.place(relx=0.30,rely=0.67,relwidth=0.40)

        #RegisterButton
        registerbtn = Button(frame, command=self.register_window,text='Register New User',font=('Sans',13,'bold'),borderwidth=0,relief=RIDGE,fg='black',bg='#e1a363',activeforeground='black',activebackground='#e1a363')
        registerbtn.place(relx=0.30,rely=0.80,relwidth=0.40)

        #forgot password
        forgetbtn = Button(frame, command=self.forgot_password_window,text='Forgot Password',font=('Sans',13,'bold'),borderwidth=0,relief=RIDGE,fg='black',bg='#e1a363',activeforeground='black',activebackground='#e1a363')
        forgetbtn.place(relx=0.30,rely=0.88,relwidth=0.40)
    
    #Use this function to create top level window which will open other parts of the application
    def register_window(self):
        #when below line executes it creates a new Toplevel empty window. That window object is stored
        #in a variable which then is used to call the Register class,which will provid all the functionality
        #to that empty window
        self.new_window = Toplevel(self.root) 
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error","All Fields Required!")
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email = %s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row  = my_cursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid Username or password')
            else:
                open_main = messagebox.askyesno("Verify yourself","Access only admin")
                if open_main > 0:
                    pass
                else: 
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    
    #----------------------Forgot Password Window------------------------------------------
    def forgot_password_window(self):
        if self.txtuser.get() == '':
            messagebox.showerror('Error','Please Enter email to reset the password')
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register where email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            print(row)
            if row == None:
                messagebox.showerror("Error","Please Enter a Valid email ID")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title('Forgot Password')
                self.root2.geometry('340x450+610+170')

                l = Label(self.root2,text='Forgot Password', font=('Sans',20,'bold'),fg='black',bg='white')
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2,text='Select Security Question',font=('Sans',15,'bold'))
                security_Q.place(x=50,y=80)
                self.combo_security_Q = ttk.Combobox(self.root2,font=('Sans',15),state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birthplace","Your Girlfriend's name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2,text='Security Answer',font=('Sans',15,'bold'))
                security_A.place(x=85,y=150)
                self.security_A_entry = ttk.Entry(self.root2,font=('Sans',15))
                self.security_A_entry.place(x=50,y=180,width=250)

                new_password = Label(self.root2,text='New Password',font=('Sans',15,'bold'))
                new_password.place(x=85,y=220)
                self.new_password_entry = ttk.Entry(self.root2,font=('Sans',15))
                self.new_password_entry.place(x=50,y=250,width=250)

                reset_button = Button(self.root2,command=self.reset_password,text='Reset Password',font=('Sans',15,'bold'),borderwidth=0,bg='green',fg='white',activebackground='green',activeforeground='white')
                reset_button.place(x=50,y=320,width=250,height=50)

#------------------Reset Function---------------------------------------------------
    def reset_password(self):
        if self.combo_security_Q.get() == 'Select':
            messagebox.showerror('Error','Select Security Question',parent=self.root2)
        elif self.security_A_entry.get() == '':
            messagebox.showerror('Error','Please Enter the Security Answer',parent=self.root2)
        elif  self.new_password_entry.get() == '':
            messagebox.showerror('Error','Please Enter a Password',parent=self.root2)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            query = ('SELECT * FROM register WHERE email=%s and securityQ=%s and securityA=%s')
            value = (self.txtuser.get(),self.combo_security_Q.get(),self.security_A_entry.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror('Error',"Incorrect Security Answer!",parent=self.root2)
            else:
                query = ('UPDATE register SET password = %s where email=%s')
                value = (self.new_password_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Your password has been reset. Please login with new password!',parent=self.root2)
                self.root2.destroy()

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

        b2 = Button(frame,text='Login Now',command=self.return_login,borderwidth=0,font=('Sans',15,'bold'),bg='green',fg='white',activebackground='green',activeforeground='white',cursor='hand2')
        b2.place(relx=0.55,rely=0.80,relheight=0.08,relwidth=0.30)
    
    #-------------------Function Declaration-----------------------------
    #Below function performs some data validation
    def register_data(self):
        if self.var_fname.get() == '' or self.var_email.get() == '' or self.var_securityQ == 'Select':
            messagebox.showerror('Error',"All fields are required!",parent=self.root)
        elif self.var_contact.get()=='' or self.var_email.get()=='':
            messagebox.showerror('Error',"All fields are required!",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must be Same!",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please Agree our terms and conditions!",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hotel_management_system')
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'User already exists, Please try another email ID!')
            else:
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
                messagebox.showinfo("Success","Registration Successful!")
    
    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    main()


