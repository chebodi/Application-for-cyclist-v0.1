import tkinter as tk
from PIL import ImageTk, Image
import sqlalchemy
from sqlalchemy import create_engine
import os
engine = create_engine('oracle://sys:12345@localhost:1521/orcl?mode=SYSDBA', echo='debug')


def Check_if_logged(login, password):
    conn = engine.connect()
    metadata = sqlalchemy.MetaData()
    division = sqlalchemy.Table('LOGOWANIE', metadata, autoload=True, autoload_with=engine)
    query = division.select().where(division.columns.HASŁO == password, division.columns.nick == login)
    output = (conn.execute(query)).fetchall()
    if len(output) == True:
        print("yes")
    else:
        print('no')


# query = sqlalchemy.insert(division).values(playerid=15, firstname='Matthew', lastname="English", sport="cric")
# Result = conn.execute(query)

def Get_Login_Password():
    login = entr_login.get()
    password = entr_password.get()
    Check_if_logged(login, password)
def Registration():
    import Registration
    os.system('Registration.py')
def add_label():
    lable1 = tk.Label(win, text='Log In')
    lable1.pack()


win = tk.Tk()

photo = tk.PhotoImage(file='cartoon-bike1.png')
win.iconphoto(False, photo)
win.config(bg='#95c6bd')
win.title('Aplikacja dla rowerzystow')
win.geometry('900x500+150+150')
win.resizable(False, False)
win.image = tk.PhotoImage(file='set-women.png')
bg_logo = tk.Label(win, image=win.image)

# bg_logo.pack(padx=0,pady=0,anchor='e')
# frame = tk.Frame(win, width=390, height=400, bg='white')
# frame.place(x=390, y=100)

lable = tk.Label(win, text='Log In',bg='#95c6bd',font=('Arial Black', 40, 'bold'),padx=120,pady=0,width=25,height=3,anchor='e')
lable.pack()

butt = tk.Button(win, text='Log In',command=Get_Login_Password, bg='#8469bd',font=('Arial Black', 15, 'bold'),padx=120,pady=0,)
butt.place(x=520, y=275)

butt = tk.Button(win, text='I wannna register',command=0, bg='#8469bd',font=('Arial Black', 15, 'bold'),padx=120,pady=0,)
butt.place(x=460, y=330)

entr_login = tk.Entry(win, text='your login',bg='#8469bd',fg='black',font=('Arial Black', 15, 'bold'),)# padx=120,# pady=0,
entr_login.place(x=555, y=175)

entr_password = tk.Entry(win, text='password',bg='#8469bd',fg='black',font=('Arial Black', 15, 'bold'), )# padx=120,# pady=0,
entr_password.place(x=555, y=225)


win.mainloop()
