from tkinter import *

expression = " "

def click(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clickequal():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = " "

    except:
        equation.set("error!")
        expression = " "

def clear():
    global expression
    expression = " "
    equation.set(" ")

if __name__=="__main__":
    window = Tk()
    window.configure(background="white")
    window.maxsize(width = 500,height = 500)
    window.title("BASIC CALCULATOR")
    equation = StringVar()

    e1 = Entry(window,bd=15,textvariable=equation)
    e1.grid(columnspan=7,ipadx=100)

    b1=Button(window,text = " 1 ",fg="black",bg="light grey",command= lambda: click(1),height=1,width=7)
    b1.grid(row=3,column=0)

    b2=Button(window,text = " 2 ",fg="black",bg="light grey",command= lambda: click(2),height=1,width=7)
    b2.grid(row=3,column=1)

    b3=Button(window,text = " 3 ",fg="black",bg="light grey",command= lambda: click(3),height=1,width=7)
    b3.grid(row=3,column=2)

    b4=Button(window,text = " 4 ",fg="black",bg="light grey",command= lambda: click(4),height=1,width=7)
    b4.grid(row=4,column=0)

    b5=Button(window,text = " 5 ",fg="black",bg="light grey",command= lambda: click(5),height=1,width=7)
    b5.grid(row=4,column=1)

    b6=Button(window,text = " 6 ",fg="black",bg="light grey",command= lambda: click(6),height=1,width=7)
    b6.grid(row=4,column=2)

    b7=Button(window,text = " 7 ",fg="black",bg="light grey",command= lambda: click(7),height=1,width=7)
    b7.grid(row=5,column=0)

    b8=Button(window,text = " 8 ",fg="black",bg="light grey",command= lambda: click(8),height=1,width=7)
    b8.grid(row=5,column=1)

    b9=Button(window,text = " 9 ",fg="black",bg="light grey",command= lambda: click(9),height=1,width=7)
    b9.grid(row=5,column=2)

    b0=Button(window,text = " 0 ",fg="black",bg="light grey",command= lambda: click(0),height=1,width=7)
    b0.grid(row=6,column=1)

    bdb=Button(window,text = " . ",fg="black",bg="light grey",command= lambda: click("."),height=1,width=7)
    bdb.grid(row=6,column=0)

    eq=Button(window,text = " = ",fg="black",bg="light grey",command=clickequal,height=1,width=7)
    eq.grid(row=6,column=2)

    plus=Button(window,text = " + ",fg="black",bg="light grey",command= lambda: click("+"),height=1,width=7)
    plus.grid(row=3,column=3)

    subtract=Button(window,text = " - ",fg="black",bg="light grey",command= lambda: click("-"),height=1,width=7)
    subtract.grid(row=4,column=3)

    multiply=Button(window,text = " * ",fg="black",bg="light grey",command= lambda: click("*"),height=1,width=7)
    multiply.grid(row=5,column=3)

    divide=Button(window,text = " / ",fg="black",bg="light grey",command= lambda: click("/"),height=1,width=7)
    divide.grid(row=6,column=3)

    clear=Button(window,text="Clear",fg="black",bg="light grey",command=clear,height=1,width=7)
    clear.grid(row=2,column=1)

    window.mainloop()

