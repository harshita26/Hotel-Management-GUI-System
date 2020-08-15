import tkinter as tk
from tkinter import ttk
import mysql.connector

root=tk.Tk()
root.title('HOTEL MANAGEMENT')
root.configure(background='#d9d9d9',highlightcolor='#000000',highlightbackground='#ffffff')
root.geometry('881x582+249+104')
# root.resizable(0,0)

# frame
main_frame=tk.Frame(root,highlightbackground='#d9d9d9',highlightcolor='black',width=921,background='#d9d9d9',borderwidth='2',relief="groove")

# label
head=tk.Label(main_frame,text='TAKE YOUR RECIPT!!',foreground='#000000',background='#d9d9d9',font=('Segoe UI',26,'bold'),width=925)
room_label=tk.Label(main_frame,text="""*********************** HOTEL AND RESORTS ***************************
**************************** ABC DELHI*****************************
************************ SERVING    GUEST   SINCE ******************
*********************************************************************""",foreground='#000000',background='#d9d9d9',font=('Segoe UI',12,'bold'),width=925)

# out
name_txt=tk.Text(main_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',14,'bold'),width=824)
conn=mysql.connector.connect(host="localhost",username='root',password='',database='HMS')
mycursur=conn.cursor()
mycursur.execute("SELECT last_insert_id() from hotel")
for row in mycursur:
   print(row)
   name_txt.insert(tk.INSERT,row)
   # name_txt.insert(tk.INSERT,"\n")
   # name_txt.insert(tk.INSERT,row[1])
   # name_txt.insert(tk.INSERT,"\n")

# place
main_frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
head.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
room_label.place(relx=0.02, rely=0.15, height=78, width=800)
name_txt.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)


root.mainloop()
