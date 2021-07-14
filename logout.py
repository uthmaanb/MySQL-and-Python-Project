from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime

root = Tk()
# widget features & style
root.geometry("450x400")
root.title("MySQL logout (Uthmaan Breda)")
root.config(bg="red")

Label(root, text='Username:', bg="red", font="poppins 10 bold").place(x=30, y=50)
user_ent = Entry(root)
user_ent.place(x=100, y=50)
Label(root, text='Password:', bg="red", font="poppins 10 bold").place(x=30, y=100)
pass_ent = Entry(root)
pass_ent.place(x=100, y=100)


def logout():
    date = datetime.now().date().strftime("%Y-%m-%d")
    time = datetime.now().time().strftime('%H:%M:%S')
    mydb = mysql.connector.connect(user='root', password='Themainp1zza!', host='127.0.0.1', database='login_lc',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("Select * from users")

    if user_ent.get() == '' or pass_ent.get() == '':
        messagebox.showerror('error', 'fill in all fields', parent=root)
    for i in mycursor:
        if user_ent.get() == i[2] and pass_ent.get() == i[3]:
            sql4 = "UPDATE login SET logout = %s WHERE username ='" + user_ent.get() + "' AND date_login='" + date + "'"
            val4 = [time]
            mycursor.execute(sql4, val4)
            mydb.commit()

            messagebox.showinfo('Success', 'You are logged out\n'
                                           ' Safe home, Straight home :)')
            root.destroy()
            import main

    else:
        messagebox.showerror('ERROR!!!!!!!!!!!', 'Incorrect credentials')


Button(root, text='Logout', command=logout, bg="red", font="poppins 10 bold", border="5").place(x=80, y=150)

root.mainloop()  # continuously runs program in window

# (ctrl + alt + L) to reformat code
