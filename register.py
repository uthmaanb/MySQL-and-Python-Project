from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
# widget features & style
root.geometry("450x700")
root.title("MySQL register (Uthmaan Breda)")
root.config(bg="red")

Label(root, text='Username:', bg="red", font="poppins 10 bold").place(x=30, y=50)
user_ent = Entry(root)
user_ent.place(x=100, y=50)
Label(root, text='Password:', bg="red", font="poppins 10 bold").place(x=30, y=100)
pass_ent = Entry(root)
pass_ent.place(x=100, y=100)
Label(root, text='name:', bg="red", font="poppins 10 bold").place(x=30, y=150)
name_ent = Entry(root)
name_ent.place(x=100, y=150)
Label(root, text='surname:', bg="red", font="poppins 10 bold").place(x=30, y=200)
surname_ent = Entry(root)
surname_ent.place(x=100, y=200)
Label(root, text='id-num:', bg="red", font="poppins 10 bold").place(x=30, y=250)
ID_ent = Entry(root)
ID_ent.place(x=100, y=250)
Label(root, text='email:', bg="red", font="poppins 10 bold").place(x=30, y=300)
mail_ent = Entry(root)
mail_ent.place(x=100, y=300)
Label(root, text='phone:', bg="red", font="poppins 10 bold").place(x=30, y=350)
cell_ent = Entry(root)
cell_ent.place(x=100, y=350)
Label(root, text='kin_name:', bg="red", font="poppins 10 bold").place(x=30, y=450)
kin_name_ent = Entry(root)
kin_name_ent.place(x=100, y=450)
Label(root, text='kin_surname:', bg="red", font="poppins 10 bold").place(x=30, y=500)
kin_surname_ent = Entry(root)
kin_surname_ent.place(x=100, y=500)
Label(root, text='kin_cell:', bg="red", font="poppins 10 bold").place(x=30, y=550)
kin_cell_ent = Entry(root)
kin_cell_ent.place(x=100, y=550)

label5 = Label(root, text="Role:")
label5.place(x=30, y=400)

option = ["lecturer", "Student"]  # set values for option list
values = StringVar(root)  # set variable to keep track of option value selected
values.set("Select an option")  # set the default value on display (a value from list can be put by saying option[0])


# Create the optionmenu widget and passing
# the option and values to it.
opt = OptionMenu(root, values, *option)
opt.config(width=15)
opt.place(x=100, y=400)


def register():
    if user_ent.get() == "" or pass_ent.get() == "" or name_ent.get() == "" or surname_ent.get() == "" or\
            ID_ent.get() == "" or mail_ent.get() == "" or cell_ent.get() == "" or values.get() == 'Select an option'\
            or kin_name_ent.get() == '' or kin_surname_ent.get() == '' or kin_cell_ent.get() == '':
        messagebox.showerror("Error", "Fill in all fields")

    else:
        mydb = mysql.connector.connect(user='root', password='Themainp1zza!', host='127.0.0.1', database='login_lc',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        sql = """
             INSERT INTO users (username, password, name, surname, id_num, email, cell, role) VALUES (%s, %s, %s,
             %s, %s, %s, %s, %s)
          """
        val = (user_ent.get(), pass_ent.get(), name_ent.get(), surname_ent.get(), ID_ent.get(), mail_ent.get(),
               cell_ent.get(), values.get())

        mycursor.execute(sql, val)
        mydb.commit()

        sql2 = "INSERT INTO next_of_kin (name, surname, cell, user_id) VALUES (%s, %s, %s, %s)"
        val2 = (kin_name_ent.get(), kin_surname_ent.get(), kin_cell_ent.get(), ID_ent.get())
        mycursor.execute(sql2, val2)
        mydb.commit()
        messagebox.showinfo('status', 'registration successful')
        root.destroy()
        import main


Button(root, text='Register', command=register, bg="red", font="poppins 10 bold", border="5").place(x=180, y=570)


root.mainloop()  # continuously runs program in window
