import tkinter as tk
from tkinter import messagebox,font,ttk
import mysql.connector
from subprocess import call

root=tk.Tk()
root.title('ADD DETAILS FOR CHECKIN')
root.configure(background='#ffffff',highlightcolor='#000000',highlightbackground='#ffffff')
root.geometry('1069x742')
# root.resizable(0,0)

class HOTEL:
   def __init__(self,name_value,address_value,contact_value,day_value):
      self.name_value=''
      self.address_value=''
      self.contact_value=0
      self.day_value=0
      self.price=0
      self.room=0

   def check_name(self):
      name_val=str(user_name.get())
      if name_val.isdigit()==False and len(name_val)>1:
         self.name_value=name_val
         text.insert(tk.INSERT,"NAME INPUT IS VALID \n")
      else:
         text.insert(tk.INSERT,"NAME INPUT IS INVALID \n")

   def check_address(self):
      add_val=str(address.get())
      if add_val.isdigit()==False and len(add_val)>1:
         self.address_value=add_val
         text.insert(tk.INSERT,"ADDRESS INPUT IS VALID \n")
      else:
         text.insert(tk.INSERT,"ADDRESS INPUT IS INVALID \n")

   def check_contact(self):
      cont_val=str(contact.get())
      if cont_val.isdigit()==True and cont_val!='' and len(cont_val)==10:
         self.contact_value=cont_val
         text.insert(tk.INSERT,"PHONE NUMBER INPUT IS VALID \n")
      else:
         text.insert(tk.INSERT,"PHONE NUMBER INPUT IS INVALID \n")

   def check_day(self):
      day_val=str(days.get())
      if day_val.isdigit() == True and len(day_val) != 0:
         self.day_value=int(day_val)
         text.insert(tk.INSERT,"DAY INPUT IS VALID \n")
      else:
         text.insert(tk.INSERT,"DAY INPUT IS INVALID \n")

   # button functionaility
   def action(self):
      m=[9]
      G=[]
      delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
      semi_delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
      full_delux = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
      joint_room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
      if room1.get()==1:
         a=delux
         m[0]=1
         self.price = self.price + (2000 * self.day_value)
      elif room2.get()==1:
         a=semi_delux
         m[0]=2
         self.price = self.price + (1500 * self.day_value)
      elif room3.get()==1:
         a=full_delux
         m[0]=3
         self.price = self.price + (1000 * self.day_value)
      elif room4.get()==1:
         m[0]=4
         a=joint_room
         self.price = self.price + (1800 * self.day_value)
      else:
         text.insert(tk.INSERT,"PLEASE ENTER VALID ROOM \n")

      if pay.get()=='bycash':
         text.insert(tk.INSERT, "NO DISCOUNT \n")
      else:
         self.price = self.price - ((self.price * 10) / 100)
         text.insert(tk.INSERT, "10% DISCOUNT \n")

      
      if len(G)>0:
         conn=mysql.connector.connect(host='localhost',username='root',password='',database='hms')
         mycursur=conn.cursor(prepared=True)
         mycursur.execute("SELECT room FROM hotel")
         q=mycursur.fetchall()
         for k in q:
            G.append(k)
         
      for r in a:
         if r not in G:
            self.room = r
            break
         else:
            continue
      self.room = r
   
      # conn=mysql.connector.connect(host="localhost",username='root',password='')
      conn=mysql.connector.connect(host="localhost",username='root',password='',database='hms')
      mycursur=conn.cursor()
      query="INSERT INTO hotel (name,address,contact,day,room,price) values(%s,%s,%s,%s,%s,%s)"
      value=(self.name_value,self.address_value,self.contact_value,self.day_value,self.room,self.price)
      # mycursur.execute("CREATE DATABASE IF NOT EXISTS hms")
      # mycursur.execute("CREATE TABLE IF NOT EXISTS hotel (name varchar(20),address varchar(50),contact int(15), day int(5),room varchar(30) primary key not null,price int(20))")
      if self.name_value=='' or self.address_value=='' or self.contact_value=='' or self.day_value=='' or pay.get()=='':
         text.insert(tk.INSERT,"PLEASE ENTER VALID INPUT \n")
      else:
         text.insert(tk.INSERT,"SUBMIT INPUT \n")
         mycursur.execute(query,value)
         mycursur.lastrowid
         call(['python','getrecipt.py'])
      conn.commit()
      mycursur.close()
      conn.close()


# frame
main_frame=tk.Frame(root,background='#ffffff',width=994,borderwidth='2',relief="groove")
main_frame.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
input_frame=tk.Frame(root,background='#ffffff',width=994,borderwidth="2",relief="groove")
input_frame.place(relx=0.03, rely=0.18, relheight=0.5, relwidth=0.93)
text=tk.Text(root,background='#ffffff',width=994)
text.config(wrap='word',relief="groove",font=('Arial',12))
text.place(relx=0.03, rely=0.7, relheight=0.25, relwidth=0.93)

# label heading
head=tk.Label(main_frame,text='YOU CLICKED ON : CHECK INN',foreground='#000000',background='#ffffff',font=('Segoe UI',30,'bold'),width=994)
head.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.93)

# label
name_label=tk.Label(input_frame,text='ENTER YOUR NAME: ',foreground='#000000',background='#ffffff',font=('Segoe UI',16,'bold'),activebackground='#ffffff',disabledforeground="#bfbfbf",activeforeground="black")
address_label=tk.Label(input_frame,text='ENTER YOUR ADDRESS: ',foreground='#000000',background='#ffffff',font=('Segoe UI',16,'bold'),activebackground='#ffffff',disabledforeground="#bfbfbf",activeforeground="black")
number_label=tk.Label(input_frame,text='ENTER YOUR NUMBER: ',foreground='#000000',background='#ffffff',font=('Segoe UI',16,'bold'),activebackground='#ffffff',disabledforeground="#bfbfbf",activeforeground="black")
day_label=tk.Label(input_frame,text='NUMBER OF DAYS: ',foreground='#000000',background='#ffffff',font=('Segoe UI',16,'bold'),activebackground='#ffffff',disabledforeground="#bfbfbf",activeforeground="black")
room_label=tk.Label(input_frame,text='CHOOSE YOUR ROOM: ',foreground='#000000',background='#ffffff',font=('Segoe UI',16,'bold'),activebackground='#ffffff',disabledforeground="#bfbfbf",activeforeground="black")
payment_label=tk.Label(input_frame,text='CHOOSE PAYMENT METHOD: ',foreground='#000000',background='#ffffff',font=('Segoe UI',16,'bold'),activebackground='#ffffff',disabledforeground="#bfbfbf",activeforeground="black")

# entry variable
user_name=tk.StringVar()
address=tk.StringVar()
contact=tk.StringVar()
days=tk.StringVar()
room1=tk.IntVar()
room2=tk.IntVar()
room3=tk.IntVar()
room4=tk.IntVar()
pay=tk.StringVar()

# entry
name_entry=tk.Entry(input_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',14),textvariable=user_name)
address_entry=tk.Entry(input_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',14),textvariable=address)
number_entry=tk.Entry(input_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',14),textvariable=contact)
day_entry=tk.Entry(input_frame,foreground='#000000',background='#ffffff',font=('Segoe UI',14),textvariable=days)

room_check1=tk.Checkbutton(input_frame,text='DELUXE',foreground='#000000', activebackground="#ffffff", background='#ffffff',font=('Segoe UI',14,'bold'),variable=room1)
room_check2=tk.Checkbutton(input_frame,text='GENERAL',foreground='#000000', activebackground="#ffffff", background='#ffffff',font=('Segoe UI',14,'bold'),variable=room2)
room_check3=tk.Checkbutton(input_frame,text='FULL DELUXE',foreground='#000000', activebackground="#ffffff", background='#ffffff',font=('Segoe UI',14,'bold'),variable=room3)
room_check4=tk.Checkbutton(input_frame,text='JOINT',foreground='#000000', activebackground="#ffffff", background='#ffffff',font=('Segoe UI',14,'bold'),variable=room4)

pay_radio1=tk.Radiobutton(input_frame,text='BY CASH',value='bycash',font=('Segoe UI',14,'bold'),foreground='#000000',background='#ffffff',activebackground='#ffffff',variable=pay)
pay_radio2=tk.Radiobutton(input_frame,text='BY CREDIT/ DEBIT CARD',value='bycredit',font=('Segoe UI',14,'bold'),foreground='#000000',background='#ffffff',activebackground='#ffffff',variable=pay)

hotel=HOTEL('','','','')

# button
nameok1_btn=tk.Button(input_frame,text='OK',font=('Segoe UI',14,'bold'),foreground= '#000000',background='#ffffff',activebackground='#ffffff',width=40,command=hotel.check_name)
addressok1_btn=tk.Button(input_frame,text='OK',font=('Segoe UI',14,'bold'),foreground= '#000000',background='#ffffff',activebackground='#ffffff',width=40,command=hotel.check_address)
contactok1_btn=tk.Button(input_frame,text='OK',font=('Segoe UI',14,'bold'),foreground= '#000000',background='#ffffff',activebackground='#ffffff',width=40,command=hotel.check_contact)
dayok1_btn=tk.Button(input_frame,text='OK',font=('Segoe UI',14,'bold'),foreground= '#000000',background='#ffffff',activebackground='#ffffff',width=40,command=hotel.check_day)
sub_btn=tk.Button(input_frame,text='SUBMIT',font=('Segoe UI',14,'bold'),foreground= '#000000',background='#ffffff',activebackground='#ffffff',width=40,command=hotel.action)

# place
name_label.place(relx=0.05, rely=0.03, height=40, width=335)
address_label.place(relx=0.05, rely=0.14, height=40, width=335)
number_label.place(relx=0.05, rely=0.26, height=40, width=335)
day_label.place(relx=0.05, rely=0.38, height=40, width=335)
room_label.place(relx=0.05, rely=0.49, height=40, width=800)
payment_label.place(relx=0.05, rely=0.76, height=40, width=800)
name_entry.place(relx=0.47,rely=0.03,height=34,relwidth=0.43)
address_entry.place(relx=0.47,rely=0.14,height=34,relwidth=0.43)
number_entry.place(relx=0.47,rely=0.26,height=34,relwidth=0.43)
day_entry.place(relx=0.47,rely=0.38,height=34,relwidth=0.43)
room_check1.place(relx=0.15, rely=0.56, relheight=0.11, relwidth=0.16)
room_check2.place(relx=0.55, rely=0.56, relheight=0.11, relwidth=0.16)
room_check3.place(relx=0.15, rely=0.67, relheight=0.11, relwidth=0.21)
room_check4.place(relx=0.55, rely=0.67, relheight=0.11, relwidth=0.16)
pay_radio1.place(relx=0.15,rely=0.85,relheight=0.11,relwidth=0.2)
pay_radio2.place(relx=0.45,rely=0.85,relheight=0.11,relwidth=0.3)
nameok1_btn.place(relx=0.91, rely=0.03, height=33, width=43)
addressok1_btn.place(relx=0.91, rely=0.14, height=33, width=43)
contactok1_btn.place(relx=0.91, rely=0.26, height=33, width=43)
dayok1_btn.place(relx=0.91, rely=0.38, height=33, width=43)
sub_btn.place(relx=0.76, rely=0.66, height=83, width=156)


root.mainloop()