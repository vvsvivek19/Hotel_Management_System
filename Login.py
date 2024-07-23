from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

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
        registerbtn = Button(frame, text='Register New User',font=('Sans',13,'bold'),borderwidth=0,relief=RIDGE,fg='black',bg='#e1a363',activeforeground='black',activebackground='#e1a363')
        registerbtn.place(relx=0.30,rely=0.80,relwidth=0.40)

        #forgot password
        forgetbtn = Button(frame, text='Forgot Password',font=('Sans',13,'bold'),borderwidth=0,relief=RIDGE,fg='black',bg='#e1a363',activeforeground='black',activebackground='#e1a363')
        forgetbtn.place(relx=0.30,rely=0.88,relwidth=0.40)
    
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error","All Fields Required!")
        elif self.txtuser.get() == 'Vivek' and self.txtpass.get() == '1234':
            messagebox.showinfo('Success!','Welcome to Hotel Taj!')
        else:
            messagebox.showerror('Invalid Credentials','Invalid Username or password!')




if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()


