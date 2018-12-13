# Author : Shaik Thowsif
# Gmail : sthowsif496@gmail.com
# Description : It is basic Calculator implementation using python gui used as desktop application

from Tkinter import *

expression = ""         #global variable declaration for expression

class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)  # init frame
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Calculator")   # title of Window
        # self.pack(fill = BOTH , expand =1)
        self.equation = StringVar()

        self.lblDisp = Entry(self.master,text=self.equation,bg="white",fg="grey",font=("Italic",15),width=30)
        self.lblDisp.pack()
        # lblDisp.place(x=0,y=0)
        # lblDisp.place(x=0,y=0)
        # lblDisp.pack_propagate(0)
        # lblDisp.place(x=0,y=0)
        # lblDisp.grid(row=0)

        buttonOne = Button(self.master,text="1",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(1))
        # buttonOne.pack()
        buttonOne.place(x=0,y=55)

        buttonTwo = Button(self.master,text="2",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(2))
        buttonTwo.place(x=100,y=55)

        buttonThree = Button(self.master,text="3",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(3))
        buttonThree.place(x=200,y=55)

        buttonClr = Button(self.master,text="CLear",justify=LEFT,width=10,height=2,padx=5,command=self.clear)
        buttonClr.place(x=300,y=55)

        #  Third Row
        buttonFour = Button(self.master,text="4",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(4))
        # buttonOne.pack()
        buttonFour.place(x=0,y=100)
        # buttonFour.grid(row=3)

        buttonFive = Button(self.master,text="5",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(5))
        buttonFive.place(x=100,y=100)
        # buttonFive.grid(row=3,column=1)

        buttonSix = Button(self.master,text="6",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(6))
        buttonSix.place(x=200,y=100)

        buttonAdd = Button(self.master,text="+",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress("+"))
        buttonAdd.place(x=300,y=100)

        # Fourth row
        buttonSeven = Button(self.master,text="7",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(7))
        # buttonOne.pack()
        buttonSeven.place(x=0,y=145)

        buttonEight = Button(self.master,text="8",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(8))
        buttonEight.place(x=100,y=145)

        buttonNine = Button(self.master,text="9",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress(9))
        buttonNine.place(x=200,y=145)

        buttonSub = Button(self.master,text="-",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress("-"))
        buttonSub.place(x=300,y=145)

        #  fifth row
        buttonEqual = Button(self.master,text="=",justify=LEFT,width=10,height=2,padx=5,command=self.equalPress)
        # buttonOne.pack()
        buttonEqual.place(x=0,y=190)

        buttonZero = Button(self.master,text="0",justify=LEFT,width=10,height=2,padx=5, command=lambda:self.self.numPress(0))
        buttonZero.place(x=100,y=190)

        buttonMul = Button(self.master,text="*",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress("*"))
        buttonMul.place(x=200,y=190)

        buttonDiv = Button(self.master,text="/",justify=LEFT,width=10,height=2,padx=5,command=lambda:self.numPress("/"))
        buttonDiv.place(x=300,y=190)

    def numPress(self,num):
        global expression
        expression = expression + str(num)
        self.equation.set(expression)
        # self.lblDisp.configure(text=num)

    def equalPress(self):
        global expression

        total = str(eval(expression))  #str eval is pridefined python function used for string(equation) evalution
        self.equation.set(total)

        expression = ""
        expression = str(total)

    def clear(self):
        global expression
        expression = ""
        self.equation.set(expression)


root = Tk()
root.geometry('400x250')
# root.title("Calculator")

app = Calculator(root)

root.mainloop()
