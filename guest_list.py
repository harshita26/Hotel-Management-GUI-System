import tkinter as tk
from tkinter import messagebox,font,ttk
import mysql.connector

root=tk.Tk()
root.title('HOTEL MANAGEMENT')
root.configure(background='#ffffff',highlightcolor='#000000',highlightbackground='#ffffff')
root.geometry('780x541+504+123')
# root.resizable(0,0)

# label frame
head=tk.LabelFrame(root,text='YOU CLICKED ON : LIST OF ALL GUEST',foreground='#000000',background='#ffffff',font=('Segoe UI',17,'bold'),width=760)
frame1=tk.Frame(head,relief="groove",borderwidth="2",width=995,background="#d9d9d9",highlightbackground="#ffffff",highlightcolor="black")
frame2=tk.Frame(head,relief="groove",borderwidth="2",width=995,background="#d9d9d9",highlightbackground="#ffffff",highlightcolor="black")

# label
name_label=tk.Label(frame1,text='NAMES: ',foreground='#000000',background="#d9d9d9",font=('Segoe UI',16,'bold'),width=335)
room_label=tk.Label(frame2,text='ROOM NUMBER: ',foreground='#000000',background="#d9d9d9",font=('Segoe UI',16,'bold'),width=330)

# text
name_txt=tk.Text(frame1,foreground='#000000',background='#ffffff',font=('Times New Roman',16,'bold'),insertbackground="black",width=314)#,state='readonly'
room_txt=tk.Text(frame2,foreground='#000000',background='#ffffff',font=('Times New Roman',16,'bold'),insertbackground="black",width=314)

# place
head.place(relx=0.01, rely=0.04, relheight=0.95, relwidth=0.97)
frame1.place(relx=0.03, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
name_label.place(relx=0.28, rely=0.02, height=37, width=117)
room_label.place(relx=0.36, rely=0.02, height=44, width=170)
name_txt.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
room_txt.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)

conn=mysql.connector.connect(host="localhost",username='root',password='',database='HMS')
mycursur=conn.cursor()
mycursur.execute("SELECT name,room FROM hotel")
for row in mycursur:
   name_txt.insert(tk.INSERT,row[0])
   name_txt.insert(tk.INSERT,"\n")
   room_txt.insert(tk.INSERT,row[1])
   room_txt.insert(tk.INSERT,"\n")
conn.commit()
mycursur.close()
conn.close()



root.mainloop()