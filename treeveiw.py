import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox


root = Tk()
root.geometry("920x650")
root.title("MySQL treeveiw (Uthmaan Breda)")


mydb = mysql.connector.connect(user='root', password='Themainp1zza!', host='127.0.0.1', database='login_lc',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM users')

tree = ttk.Treeview(root)
tree['show'] = 'headings'

ttk.Style(root).theme_use('clam')

# define columns
tree['columns'] = ('id', 'id_num', 'username', 'password', 'name', 'surname', 'email', 'cell', 'role')

# give width and anchor
tree.column('id', width=100, minwidth=100, anchor=CENTER)
tree.column('id_num', width=100, minwidth=100, anchor=CENTER)
tree.column('username', width=100, minwidth=100, anchor=CENTER)
tree.column('password', width=100, minwidth=100, anchor=CENTER)
tree.column('name', width=100, minwidth=100, anchor=CENTER)
tree.column('surname', width=100, minwidth=100, anchor=CENTER)
tree.column('email', width=100, minwidth=150, anchor=CENTER)
tree.column('cell', width=100, minwidth=100, anchor=CENTER)
tree.column('role', width=100, minwidth=100, anchor=CENTER)


# column heading
tree.heading('id', text='User-id', anchor=CENTER)
tree.heading('id_num', text='ID-Num', anchor=CENTER)
tree.heading('username', text='Username', anchor=CENTER)
tree.heading('password', text='password', anchor=CENTER)
tree.heading('name', text='Name', anchor=CENTER)
tree.heading('surname', text='Surname', anchor=CENTER)
tree.heading('email', text='Email', anchor=CENTER)
tree.heading('cell', text='Cell-Number', anchor=CENTER)
tree.heading('role', text='Role', anchor=CENTER)

i = 0
for j in mycursor:
    tree.insert('', i, text='', values=(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8]))
    i = i + 1

#  SCROLLBARs
hsb = ttk.Scrollbar(root, orient='horizontal')
hsb.config(command=tree.xview)
tree.config(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

vsb = ttk.Scrollbar(root, orient='vertical')
vsb.config(command=tree.yview)
tree.config(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)

tree.place(x=0, y=20)

# StringVar
id_num = StringVar()
username = StringVar()
password = StringVar()
name = StringVar()
surname = StringVar()
email = StringVar()
cell = StringVar()
values = StringVar()  # set variable to keep track of option value selected


def add_data(tree):
    frame = Frame(root, width=400, height=350, bg='grey')
    frame.place(x=100, y=250)
    Label(frame, text='ID').place(x=50, y=20)
    ent1 = Entry(frame, textvariable=id_num).place(x=170, y=20)
    Label(frame, text='Username').place(x=50, y=50)
    ent2 = Entry(frame, textvariable=username).place(x=170, y=50)
    Label(frame, text='Password').place(x=50, y=80)
    ent3 = Entry(frame, textvariable=password).place(x=170, y=80)
    Label(frame, text='Name').place(x=50, y=110)
    ent4 = Entry(frame, textvariable=name).place(x=170, y=110)
    Label(frame, text='Surname').place(x=50, y=140)
    ent5 = Entry(frame, textvariable=surname).place(x=170, y=140)
    Label(frame, text='Email').place(x=50, y=170)
    ent6 = Entry(frame, textvariable=email).place(x=170, y=170)
    Label(frame, text='Cell-number').place(x=50, y=200)
    ent7 = Entry(frame, textvariable=cell).place(x=170, y=200)
    Label(frame, text='Role').place(x=50, y=230)

    option = ["lecturer", "Student", 'admin']  # set values for option list
    values.set(
        "Select an option")  # set the default value on display (a value from list can be put by saying option[0])

    # Create the optionmenu widget and passing
    # the option and values to it.
    opt = OptionMenu(frame, values, *option)
    opt.config(width=15)
    opt.place(x=170, y=230)

    def insert_data():
        if id_num.get() == "" or username.get() == "" or password.get() == "" or name.get() == "" or \
                surname.get() == "" or email.get() == "" or cell.get() == "" or values.get() == 'Select an option':
            messagebox.showerror("Error", "Fill in all fields")

        nonlocal ent1, ent2, ent3, ent4, ent5, ent6, ent7, opt
        id_ = id_num.get()
        u = username.get()
        p = password.get()
        n = name.get()
        s = surname.get()
        e = email.get()
        c = cell.get()
        r = values.get()
        mycursor.execute('INSERT INTO users(id_num, username, password, name, surname, email, cell, role) VALUES(%s,'
                         ' %s, %s, %s, %s, %s, %s, %s)', (id_, u, p, n, s, e, c, r))
        mydb.commit()
        tree.insert('', 'end', text='', values=(mycursor.lastrowid, id_, u, p, n, s, e, c, r))
        messagebox.showinfo('SUCCESS', 'REGISTERED')
        id_num.set('')
        username.set('')
        password.set('')
        name.set('')
        surname.set('')
        email.set('')
        cell.set('')
        role.set('')
        frame.destroy()

    def cancel():
        frame.destroy()

    Button(frame, text='Submit', command=insert_data, bg="red", font="poppins 10 bold", border="5").place(x=100, y=280)
    Button(frame, text='Cancel', command=cancel, bg="red", font="poppins 10 bold", border="5").place(x=250, y=280)


Button(root, text='Register', command=lambda: add_data(tree), bg="red", font="poppins 10 bold", border="5").place(x=100,
                                                                                                                  y=300)
Button(root, text='admin', bg="red", font="poppins 10 bold", border="5").place(x=200, y=300)

root.mainloop()
