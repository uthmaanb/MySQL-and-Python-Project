from tkinter import *
# import mysql
import mysql.connector as mysql
from tkinter import messagebox, Text
from datetime import datetime

root = Tk()
# widget features & style
root.geometry("600x350")
root.title("MySQL (Uthmaan Breda)")
root.config(bg="#ffffff")

frame = Frame(root, width=350, height=400, bg='#346ab3')
frame.place(x=0, y=0)
Label(frame, text='Life Choices Academy', height=2, bg="#346ab3", fg='white', font=('poppins sans serif', 20,
                                                                                    'italic')).place(x=10, y=50)

name_check = False
pass_check = False


def name_text(event):
    user_ent.configure(state=NORMAL)
    user_ent.delete(0, END)
    name_check = True


def pass_text(event):
    pass_ent.configure(state=NORMAL)
    pass_ent.delete(0, END)
    pass_check = True


Label(root, text='Already have an\naccount?', height=2, bg="#ffffff", font=('poppins', 15, 'italic')).place(x=390, y=20)
user_ent = Entry(root, font=('Poppins sans serif', 27), width=10)
user_ent.insert(0, 'username')
user_ent.focus()
user_ent.bind('<Button-1>', name_text)
user_ent.place(x=370, y=93)
pass_ent = Entry(root, show="*", font=('Poppins sans serif', 27), width=10)
pass_ent.insert(0, 'password')
pass_ent.bind('<Button-1>', pass_text)
pass_ent.place(x=370, y=136)


def show_pass():
    if tick.get() == 1:
        pass_ent.configure(show="")
    if tick.get() == 0:
        pass_ent.configure(show="*")


tick = IntVar()
Checkbutton(root, variable=tick, onvalue=1, offvalue=0, command=show_pass, bg="#ffffff", borderwidth=0,
            highlightthickness=0,).place(x=370, y=190)
Label(root, text='Show password', bg="#ffffff", font=('poppins', 10, 'italic')).place(x=400, y=188)


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


Button(root, text='Log in', command=login, bg="#346ab3", fg='white', width=25, height=2, font="poppins 10 bold",
       border="0").place(x=370, y=220)
Button(root, text='Admin', command=admin, bg="#346ab3", fg='white', width=11, height=2, font="poppins 10 bold",
       border="0").place(x=370, y=280)
Button(root, text='Guest', command=guest, bg="#346ab3", fg='white', width=11, height=2, font="poppins 10 bold",
       border="0").place(x=483, y=280)


root.mainloop()  # continuously runs program in window

# (ctrl + alt + L) to reformat code
