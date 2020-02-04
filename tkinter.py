# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:41:09 2020

@author: Adminpri
"""
user1="Sirisha"
user2="Usha"
user3="Manasa"
password1="123"
password2="456"
password3="789"

def login():
    if(t1.get()==user1 and t2.get()==password1) or (t1.get()==user2 and t2.get()==password2) or (t1.get()==user3 and t2.get()==password3):
        print("welcome")
        p=t1.get()
        print(t1.get())
        window.destroy()
        window2=tk.Tk()
        window2.configure(width=500,height=500,bg='yellow')
        b2=tk.Button(window2,width=10,height=2,text="Logout",command=window2.destroy,bg='red',fg='white',font=("times",15,'bold'),activebackground="white")
        b2.place(x=220,y=300)
        lb3=tk.Label(window2,width=20,height=1,text="Welcome"+p,bg='green',fg="white",font=("times",15,'bold'))
        lb3.place(x=250,y=280)
        window2.mainloop()
    else:
        print("invalid username or password")  
def clear():
    t1.delete(0,last=len(t1.get()))
def clear1():    
    t2.delete(0,last=len(t2.get()))  
       
        
import tkinter as tk
window=tk.Tk()
window.configure(width=500,height=500,bg='yellow')
lp1=tk.Label(window,width=20,height=1,text="Enter your Name",bg='red',fg="white",font=("times",15,'bold'))
lp1.place(x=50,y=100)
lp2=tk.Label(window,width=20,height=1,text="Password",bg='red',fg="white",font=("times",15,'bold'))
lp2.place(x=50,y=200)
t1=tk.Entry(window,width=20,fg='purple',bg='blue',font=("times",15,'bold'))
t1.place(x=300,y=100)
t2=tk.Entry(window,width=20,fg='purple',bg='blue',font=("times",15,'bold'))
t2.place(x=300,y=200)
b1=tk.Button(window,width=10,height=1,text="Login",command=login,bg='red',fg='white',font=("times",15,'bold'),activebackground="white")
b1.place(x=220,y=300)
b2=tk.Button(window,width=10,text="Clear",command=clear,bg='purple',fg='white',font=("times",15,'bold'),activebackground="white")
b2.place(x=550,y=100)
b3=tk.Button(window,width=10,text="Clear",command=clear1,bg='purple',fg='white',font=("times",15,'bold'),activebackground="white")
b3.place(x=550,y=200)
window.mainloop()
