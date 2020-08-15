import tkinter as tk
from tkinter import messagebox,font,ttk
import mysql.connector

root=tk.Tk()
root.title('HOTEL MANAGEMENT')
root.configure(background='#d9d9d9',highlightcolor='#000000',highlightbackground='#ffffff')
root.geometry('881x582+249+104')
# root.resizable(0,0)

# frame
main_frame=tk.Frame(root,highlightbackground='#d9d9d9',highlightcolor='black',width=921,background='#d9d9d9',borderwidth='2',relief="groove")

# label
head=tk.Label(main_frame,text='GET INFO HERE!!',foreground='#000000',background='#d9d9d9',font=('Segoe UI',28,'bold'),width=925)
room_label=tk.Label(main_frame,text='ENTER THE ROOM NUMBER: ',foreground='#000000',background='#d9d9d9',font=('Segoe UI',22,'bold'),width=450)

room=tk.StringVar()

# entry
room_entry=tk.Entry(main_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',22),insertbackground="black",textvariable=room)

def action():
   room_no=str(room.get())
   if room_no.isdigit() == True and len(room_no) != 0:
      quer="SELECT * FROM hotel where room=%s"
      val=(room_no,)
      try:
         conn=mysql.connector.connect(host="localhost",username='root',password='',database='HMS')
         mycurs=conn.cursor()         
         mycurs.execute(quer,val)
         row=mycurs.fetchone()
         if mycurs.rowcount>0:
            out_txt.insert(tk.INSERT,f"NAME :{row[0]}, ADDRESS: {row[1]},CONTACT NUMBER: {row[2]},NUMBERS OF DAYS: {row[3]}, ROOM :{row[4]} and PRICE: {row[5]}\n")
         else:
            out_txt.insert(tk.INSERT,"NO DATA AVAILABLE \n")  
         mycurs.close()
         conn.close()       
      except Exception as e:
         print(e)
   else:
      out_txt.insert(tk.INSERT,"ENTER VALID ROOM NUMBER \n")

# button
check_btn=tk.Button(main_frame,text="SUBMIT",foreground='#000000',background='#d9d9d9',font=('Segoe UI',20,'bold'),activebackground="#ffffff",command=action)

# out
out_txt=tk.Text(main_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',14,'bold'),width=824)

# place
main_frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
head.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
room_label.place(relx=0.12, rely=0.15, height=48, width=400)
room_entry.place(relx=0.65, rely=0.17,height=40, relwidth=0.1)
check_btn.place(relx=0.39, rely=0.29, height=74, width=197)
out_txt.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)


root.mainloop()