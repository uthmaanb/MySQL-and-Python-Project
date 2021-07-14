from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
# widget features & style
root.geometry("450x700")
root.title("MySQL register (Uthmaan Breda)")
root.config(bg="red")

# StringVar
id_num = StringVar()
username = StringVar()
password = StringVar()
name = StringVar()
surname = StringVar()
email = StringVar()
cell = StringVar()
kin_name = StringVar()
kin_surname = StringVar()
kin_cell = StringVar()


Label(root, text='ID-Num:', bg="red", font="poppins 10 bold").place(x=30, y=50)
ent1 = Entry(root, textvariable=id_num).place(x=100, y=50)
Label(root, text='Username:', bg="red", font="poppins 10 bold").place(x=30, y=100)
ent2 = Entry(root, textvariable=username).place(x=100, y=100)
Label(root, text='Password:', bg="red", font="poppins 10 bold").place(x=30, y=150)
ent3 = Entry(root, textvariable=password).place(x=100, y=150)
Label(root, text='Name:', bg="red", font="poppins 10 bold").place(x=30, y=200)
ent4 = Entry(root, textvariable=name).place(x=100, y=200)
Label(root, text='Surname:', bg="red", font="poppins 10 bold").place(x=30, y=250)
ent5 = Entry(root, textvariable=surname).place(x=100, y=250)
Label(root, text='Email:', bg="red", font="poppins 10 bold").place(x=30, y=300)
ent6 = Entry(root, textvariable=email).place(x=100, y=300)
Label(root, text='Cell-Number:', bg="red", font="poppins 10 bold").place(x=30, y=350)
ent7 = Entry(root, textvariable=cell).place(x=100, y=350)
Label(root, text='kin_name:', bg="red", font="poppins 10 bold").place(x=30, y=450)
ent8 = Entry(root, textvariable=kin_name).place(x=100, y=450)
Label(root, text='kin_surname:', bg="red", font="poppins 10 bold").place(x=30, y=500)
ent9 = Entry(root, textvariable=kin_surname).place(x=100, y=500)
Label(root, text='kin_cell:', bg="red", font="poppins 10 bold").place(x=30, y=550)
ent10 = Entry(root, textvariable=kin_cell).place(x=100, y=550)


mydb = mysql.connector.connect(user='root', password='Themainp1zza!', host='127.0.0.1', database='login_lc',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def register():
    if id_num.get() == "" or username.get() == "" or password.get() == "" or name.get() == "" or \
            surname.get() == "" or email.get() == "" or cell.get() == "":
        messagebox.showerror("Error", "Fill in all fields")

    # nonlocal ent1, ent2, ent3, ent4, ent5, ent6, ent7
    id_ = id_num.get()
    u = username.get()
    p = password.get()
    n = name.get()
    s = surname.get()
    e = email.get()
    c = cell.get()
    mycursor.execute('INSERT INTO users(id_num, username, password, name, surname, email, cell, role) VALUES(%s,'
                     ' %s, %s, %s, %s, %s, %s, %s)', (id_, u, p, n, s, e, c, 'visitor'))
    mydb.commit()

    sql2 = "INSERT INTO next_of_kin (name, surname, cell, user_id) VALUES (%s, %s, %s, %s)"
    val2 = (kin_name.get(), kin_surname.get(), kin_cell.get(), id_num.get())
    mycursor.execute(sql2, val2)
    mydb.commit()

    messagebox.showinfo('SUCCESS', 'REGISTERED')
    id_num.set('')
    username.set('')
    password.set('')
    name.set('')
    surname.set('')
    email.set('')
    cell.set('')
    kin_name.set('')
    kin_surname.set('')
    kin_cell.set('')


Button(root, text='Register', command=register, bg="red", font="poppins 10 bold", border="5").place(x=180, y=570)


root.mainloop()  # continuously runs program in window
