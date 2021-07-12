from tkinter import *
import mysql
import mysql.connector
from tkinter import messagebox
from datetime import datetime

root = Tk()
# widget features & style
root.geometry("450x400")
root.title("MySQL (Uthmaan Breda)")
root.config(bg="red")

Label(root, text='Username:', bg="red", font="poppins 10 bold").place(x=30, y=50)
user_ent = Entry(root)
user_ent.place(x=100, y=50)
Label(root, text='Password:', bg="red", font="poppins 10 bold").place(x=30, y=100)
pass_ent = Entry(root)
pass_ent.place(x=100, y=100)


def admin():
    root.destroy()
    import admin


def login():
    date = datetime.now().date().strftime("%Y-%m-%d")
    time = datetime.now().time().strftime('%H:%M:%S')
    mydb = mysql.connector.connect(user='root',
                                   password='Themainp1zza!',
                                   host='127.0.0.1',
                                   database='login_lc',
                                   auth_plugin='mysql_native_password',
                                   buffered=TRUE)
    mycursor = mydb.cursor()

    if user_ent.get() == '' or pass_ent.get() == '':
        messagebox.showerror('error', 'fill in all fields', parent=root)

    mycursor.execute('Select username, password from users')
    for i in mycursor:
        if user_ent.get() == i[0] and pass_ent.get() == i[1]:

            sql = "INSERT INTO login (username, date_login, login) VALUES (%s, %s, %s)"
            val = (user_ent.get(), date, time)

            mycursor.execute(sql, val)
            mydb.commit()

            messagebox.showinfo('Success', 'You are logged in')
            root.destroy()
            import logout

    else:
        messagebox.showerror('ERROR!!!!!!!!!!!', 'Incorrect credentials')


root.mainloop()  # continuously runs program in window
