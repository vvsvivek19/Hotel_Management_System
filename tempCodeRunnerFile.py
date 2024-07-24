    def reset_password(self):
        if self.combo_security_Q.get() == 'Select':
            messagebox.showerror('Error','Select Security Question')
        elif self.combo_security_Q.get() == '':
            messagebox.showerror('Error','Please Enter the Security Answer')
        elif  self.new_password_entry.get() == '':
            messagebox.showerror('Error','Please Enter a Password')
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='Vivek1465',database='hospital_management_system')
            my_cursor = conn.cursor()
            query = ('SELECT * FROM register WHERE email=%s and securityQ=%s and securityA=%s')
            value = (self.txtuser.get(),self.combo_security_Q.get(),self.security_A_entry.get())
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror('Error',"Incorrect Security Answer!")
            else:
                query = ('UPDATE register SET password = %s where email=%s')
                value = (self.new_password_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Your password has been reset. Please login with new password!')