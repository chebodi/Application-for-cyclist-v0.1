# from tkinter import *
#
# base = Tk()
# base.geometry('500x500')
# base.title("Registration Form")
#
# labl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
# labl_0.place(x=90, y=53)
#
# labl_1 = Label(base, text="FullName", width=20, font=("bold", 10))
# labl_1.place(x=80, y=130)
#
# entry_1 = Entry(base)
# entry_1.place(x=240, y=130)
#
# labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
# labl_2.place(x=68, y=180)
#
# entry_02 = Entry(base)
# entry_02.place(x=240, y=180)
#
# labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
# labl_3.place(x=70, y=230)
# var = IntVar()
# Radiobutton(base, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
# Radiobutton(base, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
#
# labl_4 = Label(base, text="Age:", width=20, font=("bold", 10))
# labl_4.place(x=70, y=280)
#
# entry_02 = Entry(base)
# entry_02.place(x=240, y=280)
#
# Button(base, text='Submit', width=20, bg='brown', fg='white').place(x=180, y=380)
# # it will be used for displaying the registration form onto the window
# base.mainloop()
# print("Registration form is created seccussfully...")

import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pandas as pd
import cx_Oracle
engine = create_engine('oracle://sys:12345@localhost:1521/orcl?mode=SYSDBA', echo='debug')
# engine = sqlalchemy.create_engine(db)                                                                                                    #con = cx_Oracle.connect('sys/12345@localhost')
#
# from sqlalchemy.sql import text
# sql = '''
#     SELECT * FROM table;
# '''
# with engine.connect().execution_options(autocommit=True) as conn:
#     query = conn.execute(text(sql))
# # df = pd.DataFrame(query.fetchall())
conn = engine.connect()#############################################1
metadata = sqlalchemy.MetaData()
division = sqlalchemy.Table('LOGOWANIE', metadata, autoload=True, autoload_with=engine)

#print(repr(metadata.tables['PLAYER']))
#print(division.columns.keys())
#query = division.select().where(division.columns.HASŁO == "abc",division.columns.nick == "B13")
# output = (conn.execute(query)).fetchall()
# if len(output) == True:
#     print("yes")
# else:
#     print('no')

#print(output)
#query = division.select().where(division.columns.haslo == 'abc')



# sql = """
#     SELECT nick FROM Logowanie WHERE ROWNUM = 1
# """
# df_orders = pd.read_sql(sql, engine)
#print(df_orders)



# with engine.connect().execution_options(autocommit=True) as conn:
#     output = conn.execute(text(sql))
# df = pd.DataFrame(output.fetchall())
#print(output.fetchall())



query = sqlalchemy.insert(division).values( HASŁO='abc5', nick="Eng")
Result = conn.execute(query)
print(len(Result))