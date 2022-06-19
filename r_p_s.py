from tkinter import *
import random
import time
import threading

w = Tk()
w.title('Rock Paper And Scissors Game')
w.geometry('500x350')
w.resizable(False,False)



user_c = ""
comp_c = ""
weapons = ["rock", "paper", "scissors"]
winner = ["paper", "scissors", "rock"]
loser = ["scissors", "rock", "paper"]


def control():
  index = weapons.index(comp_c)
  result = ""
  if(user_c ==  winner[index]):
    result = "You won!"
  elif(user_c ==  loser[index]):
    result = "You lost..."
  else:
    result = "Draw."

  l_res.config(text=result)
  l_res.place(x=175,y=105)

def set_comp_c():
  l_res.config(text= "      -")
  global comp_c
  comp_c = random.choice(weapons)
  for y in range(2):
    
    for i in range(1,4):
      l_comp.config(text="Computer's choice is "+"."*i)
      time.sleep(0.2)
    time.sleep(0.2)
    


  l_comp.config(text="Computer's choice is "+ comp_c+ " .")
  time.sleep(0.2)
  control()

def set_user_c_rk():
  global user_c
  user_c = "rock"
  set_user_l()

def set_user_c_ppr():
  global user_c
  user_c = "paper"
  set_user_l()

def set_user_c_scs():
  global user_c
  user_c = "scissors"
  set_user_l()

def set_user_l():
  l_user.config(text="Your choice is "+user_c+" .")
  x = threading.Thread(target=set_comp_c, daemon=True)
  x.start()
  

r_photo = PhotoImage(file='rk.png')
p_photo = PhotoImage(file='ppr.png')
s_photo = PhotoImage(file='scs.png')


w.iconphoto(True, p_photo)



r_btn = Button(w, text="Rock",
 font=('comic sans',20,'bold'), 
 fg='#3c5c55',
 width=100,
 height=150,
 image=r_photo,
  compound='bottom',
  relief=SOLID,
  command=set_user_c_rk)

p_btn = Button(w, text="Paper",
 font=('comic sans',20,'bold'), 
 fg='#46a38f',
 width=100,
 height=150,
 image=p_photo,
  compound='bottom',
  relief=SOLID,
  command=set_user_c_ppr)

s_btn = Button(w, text="Scissors",
 font=('comic sans',15,'bold'), 
 fg='#1ce8bc',
 width=100,
 height=150,
 image=s_photo,
  compound='bottom',
  relief=SOLID,
  command=set_user_c_scs)

buttons = [r_btn,p_btn,s_btn]

r_btn.place(x=50,y=180)
p_btn.place(x=200,y=180)
s_btn.place(x=350,y=180)

l_user = Label(w, text="Your choice is ...",
 font=('comic sans',20,'bold'),
 fg="gray",
 )
l_user.place(x=100,y=25)

l_comp =Label(w, text="Computer's choice is ...",
 font=('comic sans',20,'bold'))
l_comp.place(x=50,y=65)

l_res = Label(w, font=('comic sans',20,'bold'))



w.mainloop()
