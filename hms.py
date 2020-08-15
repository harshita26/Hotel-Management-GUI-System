import tkinter as tk
from tkinter import messagebox,font,ttk
from subprocess import call

root=tk.Tk()
root.title('HOTEL MANAGEMENT')
root.geometry('963x749+540+110')
root.configure(background='#d9d9d9',highlightcolor='black',highlightbackground='#d9d9d9')
# root.resizable(0,0)

# button action
def check_in_action():
   call(['python','check.py'])
def guest_list_action():
   call(['python','guest_list.py'])
def check_out_action():
   call(['python','checkout.py'])
def guset_info_action():
   call(['python','guestinfo.py'])

# frame
main_frame=tk.Frame(root,highlightbackground='#d9d9d9',highlightcolor='black',width=921,background='#d9d9d9',borderwidth='2',relief="groove")
main_frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)

# label
head=tk.Label(main_frame,text='WELCOME',font=('Segoe UI',40,'bold'),background='#d9d9d9',highlightcolor='black',highlightbackground='#d9d9d9',fg='#000000',width=791)
head.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)

# buttons
checkin_btn=tk.Button(main_frame,text='1. CHECK INN',highlightbackground='#d9d9d9',highlightcolor='black',background='#d9d9d9',width=566,activebackground='#d9d9d9',activeforeground='#000000',foreground='#000000',disabledforeground='#bfbfbf',font=('Segoe UI',15,'bold'),pady='2',command=check_in_action)

guestlist_btn=tk.Button(main_frame,text='2. SHOW GUEST LIST',highlightbackground='#d9d9d9',highlightcolor='black',background='#d9d9d9',width=566,activebackground='#d9d9d9',activeforeground='#000000',foreground='#000000',disabledforeground='#bfbfbf',font=('Segoe UI',15,'bold'),pady='2',command=guest_list_action)

checkout_btn=tk.Button(main_frame,text='3. CHECK OUT',highlightbackground='#d9d9d9',highlightcolor='black',background='#d9d9d9',width=566,activebackground='#d9d9d9',activeforeground='#000000',foreground='#000000',disabledforeground='#bfbfbf',font=('Segoe UI',15,'bold'),pady='2',command=check_out_action)

guestinfo_btn=tk.Button(main_frame,text='4. GET INFO OF ANY GUEST',highlightbackground='#d9d9d9',highlightcolor='black',background='#d9d9d9',width=566,activebackground='#d9d9d9',activeforeground='#000000',foreground='#000000',disabledforeground='#bfbfbf',font=('Segoe UI',15,'bold'),pady='2',command=guset_info_action)

exit_btn=tk.Button(main_frame,text='5. EXIT',highlightbackground='#d9d9d9',highlightcolor='black',background='#d9d9d9',width=566,activebackground='#d9d9d9',activeforeground='#000000',foreground='#000000',disabledforeground='#bfbfbf',font=('Segoe UI',15,'bold'),pady='2',command=quit)

# place
checkin_btn.place(relx=0.18, rely=0.17, height=95, width=566)
guestlist_btn.place(relx=0.18, rely=0.31,height=95,width=566)
checkout_btn.place(relx=0.18, rely=0.45,height=95,width=566)
guestinfo_btn.place(relx=0.18,rely=0.59,height=95,width=566)
exit_btn.place(relx=0.18,rely=0.73,height=95,width=566)


root.mainloop()