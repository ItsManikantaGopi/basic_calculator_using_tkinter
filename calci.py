from tkinter import *
from math import *
window=Tk()
#window.state("zoomed")
window.title("calculator")
window.geometry("322x463")
global exp
exp=""
def press(num):
    global exp
    exp=exp+str(num)
    eq.set(exp)
def equipress():
    try:
        global exp
        b=eval(str(exp))
        total=str(b)
        eq.set(total)
        exp=str(b)
    except:
        eq.set("invalid syntax")
        exp=""
def clr():
    global exp
    exp=""
    eq.set("")
def Del():
	global exp
	exp=exp[:-1]
	eq.set(exp)
def clr():
	global exp
	exp=""
	eq.set(exp)

eq=StringVar()
exp_field=Entry(window,textvariable=eq)
exp_field.grid(columnspan=7,rowspan=3,ipadx=100,ipady=10)
eq.set("enter you exp here!")
sr=Button(window,text="")
btp=Button(window,text="+",height=5,width=10,command=lambda:press("+")).grid(column=0,row=3)
bts=Button(window,text="-",height=5,width=10,command=lambda:press("-")).grid(column=0,row=4)
btm=Button(window,text="*",height=5,width=10,command=lambda:press("*")).grid(column=0,row=5)
btd=Button(window,text="/",height=5,width=10,command=lambda:press("/")).grid(column=0,row=6)
bt0=Button(window,text="0",height=5,width=10,command=lambda:press(0)).grid(column=2,row=6)
bt1=Button(window,text="1",height=5,width=10,command=lambda:press(1)).grid(column=1,row=5)
bt2=Button(window,text="2",height=5,width=10,command=lambda:press(2)).grid(column=2,row=5)
bt3=Button(window,text="3",height=5,width=10,command=lambda:press(3)).grid(column=3,row=5)
bt4=Button(window,text="4",height=5,width=10,command=lambda:press(4)).grid(column=1,row=4)
bt5=Button(window,text="5",height=5,width=10,command=lambda:press(5)).grid(column=2,row=4)
bt6=Button(window,text="6",height=5,width=10,command=lambda:press(6)).grid(column=3,row=4)
bt7=Button(window,text="7",height=5,width=10,command=lambda:press(7)).grid(column=1,row=3)
bt8=Button(window,text="8",height=5,width=10,command=lambda:press(8)).grid(column=2,row=3)
bt9=Button(window,text="9",height=5,width=10,command=lambda:press(9)).grid(column=3,row=3)
btfp=Button(window,text=".",height=5,width=10,command=lambda:press(".")).grid(column=1,row=6)
bte=Button(window,text="=",height=5,width=10,command=lambda:equipress()).grid(column=3,row=6)
btbrb=Button(window,text="(",height=5,width=10,command=lambda:press("(")).grid(column=0,row=7)
btbre=Button(window,text=")",height=5,width=10,command=lambda:press(")")).grid(column=1,row=7)
btdel=Button(window,text="Del",height=5,width=10,command=lambda:Del()).grid(column=2,row=7)
btclr=Button(window,text="clr",height=5,width=10,command=lambda:clr()).grid(column=3,row=7)
window.mainloop()
