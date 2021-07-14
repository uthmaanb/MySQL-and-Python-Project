import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox, simpledialog

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
kin_name = StringVar()
kin_surname = StringVar()
kin_cell = StringVar()


def add_data(tree):
    frame = Frame(root, width=700, height=350, bg='grey')
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
        "Select option")  # set the default value on display (a value from list can be put by saying option[0])

    def activate(value):
        values.set(value)
        if value == "admin":
            msg = messagebox.askquestion('ALERT!', 'Grant user Admin priveledges?')
            if msg == 'yes':
                pass_word = simpledialog.askstring("Input", "admin password",
                                                   parent=root)
                if pass_word is not None:
                    for x in mycursor:
                        if pass_word == x[3] and x[8] == 'admin':
                            messagebox.showinfo('SUCCESS', 'Successfully added admin.')
                else:
                    frame.destroy()
            elif msg == 'no':
                frame.destroy()

    # Create the optionmenu widget and passing
    # the option and values to it.
    opt = OptionMenu(frame, values, *option, command=activate)
    opt.config(width=15)
    opt.place(x=170, y=230)

    Label(frame, text='kin_name:', bg="red", font="poppins 10 bold").place(x=350, y=20)
    ent8 = Entry(frame, textvariable=kin_name).place(x=470, y=20)
    Label(frame, text='kin_surname:', bg="red", font="poppins 10 bold").place(x=350, y=50)
    ent9 = Entry(frame, textvariable=kin_surname).place(x=470, y=50)
    Label(frame, text='kin_cell:', bg="red", font="poppins 10 bold").place(x=350, y=80)
    ent10 = Entry(frame, textvariable=kin_cell).place(x=470, y=80)

    def insert_data():
        if id_num.get() == "" or username.get() == "" or password.get() == "" or name.get() == "" or \
                surname.get() == "" or email.get() == "" or cell.get() == "" or values.get() == 'Select option':
            messagebox.showerror("Error", "Fill in all fields")

        nonlocal ent1, ent2, ent3, ent4, ent5, ent6, ent7, opt, ent8, ent9, ent10
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
        values.set('Select option')
        kin_name.set('')
        kin_surname.set('')
        kin_cell.set('')
        frame.destroy()

    def cancel():
        frame.destroy()

    Button(frame, text='Submit', command=insert_data, bg="red", font="poppins 10 bold", border="5").place(x=100, y=280)
    Button(frame, text='Cancel', command=cancel, bg="red", font="poppins 10 bold", border="5").place(x=250, y=280)


def cancel():
    root.destroy()
    import main


def kill():
    root.destroy()


Button(root, text='Register', command=lambda: add_data(tree), bg="red", font="poppins 10 bold", border="5").place(x=100,
                                                                                                                  y=300)
Button(root, text='cancel', command=cancel, bg="red", font="poppins 10 bold", border="5").place(x=200, y=300)
Button(root, text='exit', command=kill, bg="red", font="poppins 10 bold", border="5").place(x=300, y=300)


root.mainloop()
