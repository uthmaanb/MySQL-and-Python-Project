from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime

root = Tk()
# widget features & style
root.geometry("600x350")
root.title("MySQL logout (Uthmaan Breda)")
root.config(bg="#ffffff")

frame = Frame(root, width=350, height=400, bg='#346ab3')
frame.place(x=0, y=0)
Label(frame, text='Life Choices Academy', height=2, bg="#346ab3", fg='white', font=('poppins sans serif', 20, 'italic')).place(x=10, y=50)

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


Label(root, text='Enjoy the rest of\nyour day.', height=2, bg="#ffffff", font=('poppins', 15, 'italic')).place(x=390, y=20)
user_ent = Entry(root, font=('Poppins sans serif', 27), width=10)
user_ent.insert(0, 'username')
user_ent.bind('<Button-1>', name_text)
user_ent.place(x=370, y=93)
pass_ent = Entry(root, font=('Poppins sans serif', 27), width=10)
pass_ent.insert(0, 'password')
pass_ent.bind('<Button-1>', pass_text)
pass_ent.place(x=370, y=136)


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


Button(root, text='Log out', command=logout, bg="#346ab3", fg='white', width=25, height=2, font="poppins 10 bold",
       border="0").place(x=370, y=220)

root.mainloop()  # continuously runs program in window

# (ctrl + alt + L) to reformat code
