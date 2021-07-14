from tkinter import *
# import mysql
import mysql.connector as mysql
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
    try:
        mydb = mysql.connect(user='root',
                             password='Themainp1zza!',
                             host='127.0.0.1',
                             database='login_lc',
                             auth_plugin='mysql_native_password',
                             buffered=True)

        cursor = mydb.cursor()
        cursor.execute("Select * from users")

        date = datetime.now().date().strftime("%Y-%m-%d")
        time = datetime.now().time().strftime('%H:%M:%S')

        if user_ent.get() == "" or pass_ent.get() == "":
            messagebox.showerror("Error!", "Fill in all fields")
        for i in cursor:
            if user_ent.get() == i[2] and pass_ent.get() == i[3]:
                sql = "INSERT INTO login (username, date_login, login) VALUES (%s, %s, %s)"
                values = (user_ent.get(), date, time)
                cursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("STATUS", "Access Granted. Welcome " + str(user_ent.get()))
                root.destroy()
                import logout
        else:
            messagebox.showerror("ERROR", "Access Denied")

    except mysql.Error as err:  # This except statement will catch all mysql errors
        messagebox.showerror("Error", "Something went wrong: " + str(err))


def guest():
    root.destroy()
    import guest_register


Button(root, text='Login', command=login, bg="red", font="poppins 10 bold", border="5").place(x=80, y=150)
Button(root, text='admin', command=admin, bg="red", font="poppins 10 bold", border="5").place(x=180, y=150)
Button(root, text='login as guest', command=guest, bg="red", font="poppins 10 bold", border="5").place(x=280, y=150)


root.mainloop()  # continuously runs program in window

# (ctrl + alt + L) to reformat code
