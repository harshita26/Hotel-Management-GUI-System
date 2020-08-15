import tkinter as tk
from tkinter import messagebox,font,ttk
import mysql.connector

root=tk.Tk()
root.title('HOTEL MANAGEMENT')
root.configure(background='#ffffff',highlightcolor='#000000',highlightbackground='#ffffff')
root.geometry('1011x750')
# root.resizable(0,0)

# input_frame.place(relx=0.03, rely=0.18, relheight=0.5, relwidth=0.93)
# label frame
main_frame=tk.Frame(root,background='#ffffff',width=925,borderwidth='2',relief="groove")
input_frame=tk.Frame(root,background='#ffffff',width=925,borderwidth='2',relief="groove")

# label
head=tk.Label(main_frame,text='YOU CLICKED ON : CHECK OUT',foreground='#000000',background='#ffffff',font=('Segoe UI',17,'bold'),width=925)
room_label=tk.Label(input_frame,text='ENTER THE ROOM NUMBER: ',foreground='#000000',background='#ffffff',font=('Segoe UI',17,'bold'),width=442)

room=tk.StringVar()

# entry
room_entry=tk.Entry(input_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',17),insertbackground="black",textvariable=room)

def action():
   room_no=str(room.get())
   if room_no.isdigit() == True and len(room_no) != 0:
      query="SELECT * FROM hotel where room=%s"
      val=(room_no,)
      try:
         conn=mysql.connector.connect(host="localhost",user='root',password='',database='hms')
         mycurs=conn.cursor(prepared=True)         
         mycurs.execute(query,val)
         print(mycurs.fetchone())
         if mycurs.rowcount>0:
            query="DELETE FROM hotel WHERE room=%s"
            val=(room_no,)
            conn=mysql.connector.connect(host="localhost",user='root',password='',database='hms')
            mycurs=conn.cursor(prepared=True)
            mycurs.execute(query,val)
            out_txt.insert(tk.INSERT,"YOU CHECKED OUT YOUR ROOM")
         else:
            out_txt.insert(tk.INSERT,"NO DATA AVAILABLE \n")   
         mycurs.close()
         conn.close()      
      except Exception as e:
         print(e)
   else:
      out_txt.insert(tk.INSERT,"ENTER VALID ROOM NUMBER \n")

# button
check_btn=tk.Button(input_frame,text="CHECK OUT",foreground='#000000',background='#ffffff',font=('Segoe UI',17,'bold'),activebackground="#ffffff",command=action)

# out
out_txt=tk.Text(input_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',17,'bold'),width=824)

# place
main_frame.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.91)
input_frame.place(relx=0.03, rely=0.18,  relheight=0.81, relwidth=0.91)
head.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.93)
room_label.place(relx=0.14, rely=0.12, height=46, width=442)
room_entry.place(relx=0.67, rely=0.12,height=44, relwidth=0.07)
check_btn.place(relx=0.34, rely=0.3, height=93, width=286)
out_txt.place(relx=0.05, rely=0.54, relheight=0.38, relwidth=0.89)




root.mainloop()