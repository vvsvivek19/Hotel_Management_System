img2 = Image.open(r'D:\Dev Role Prep\Projects\Hotel_Management_System\Images\Hotel_Logo.png')
        img2 = img2.resize((200,140),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        
        lbl_img2 = Label(self.root, image=self.photoimage2,bd=3,relief=RIDGE)
        lbl_img2.place(x=0,y=0,width=200,height=140)