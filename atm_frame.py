from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class atm:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(110 * blank_space + "KUDA BANK")
        self.root.geometry("760x650+280+0")
        self.root.configure(bg="gainsboro")
        #**************************frames******************************
        MainFrame = Frame(self.root, bd=20, width=784, height=700,
                          relief=RIDGE)
        MainFrame.grid()
        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300,
                          relief=RIDGE)
        TopFrame1.grid(row=1,column=0, padx=4)
        
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300,
                          relief=RIDGE)
        TopFrame2.grid(row=0,column=0, padx=4)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300,
                          relief=RIDGE)
        TopFrame2Left.grid(row=0,column=0, padx=2)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300,
                          relief=RIDGE)
        TopFrame2Mid.grid(row=0,column=1, padx=2)

        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300,
                          relief=RIDGE)
        TopFrame2Right.grid(row=0,column=2, padx=2)
# *******************************************************************************8
        #***********************middle_Text_widgets*****************************
        self.txtReceipt = Text(TopFrame2Mid, height = 17, width=41, bd=12,
                               font=("arial",9,"bold"))
        self.txtReceipt.grid(row=0, column=0)

        #**************************Left_widgets*****************************
        
        self.img_arrow_Left = PhotoImage(file=r"ATM_Icon\\lArrow.png")

        self.btnArrow_Left = Button(TopFrame2Left,width=160, height=60,
          image=self.img_arrow_Left, state=DISABLED).grid(row=0,column=0,padx=2,pady=1)

        self.btnArrow_Left1 = Button(TopFrame2Left,width=160, height=60,
          image=self.img_arrow_Left, state=DISABLED).grid(row=1,column=0,padx=2,pady=1)

        self.btnArrow_Left2 = Button(TopFrame2Left,width=160, height=60,
          image=self.img_arrow_Left, state=DISABLED).grid(row=2,column=0,padx=2,pady=1)

        self.btnArrow_Left3 = Button(TopFrame2Left,width=160, height=60,
          image=self.img_arrow_Left, state=DISABLED).grid(row=3,column=0,padx=2,pady=1)

        #**************************Right_widgets*****************************
        self.img_arrow_right = PhotoImage(file=r"ATM_Icon\\rArrow.png")

        self.btnArrow_Right = Button(TopFrame2Right,width=160, height=60,
          image=self.img_arrow_right, state=DISABLED).grid(row=0,column=0,padx=2,pady=1)

        self.btnArrow_Right1 = Button(TopFrame2Right,width=160, height=60,
          image=self.img_arrow_right, state=DISABLED).grid(row=1,column=0,padx=2,pady=1)

        self.btnArrow_Right2 = Button(TopFrame2Right,width=160, height=60,
          image=self.img_arrow_right, state=DISABLED).grid(row=2,column=0,padx=2,pady=1)

        self.btnArrow_Right3 = Button(TopFrame2Right,width=160, height=60,
          image=self.img_arrow_right, state=DISABLED).grid(row=3,column=0,padx=2,pady=1)


       #**************************Pin number buttons*****************************
        self.img1 = PhotoImage(file=r"ATM_Icon\\one.png")
        self.btn1 = Button(TopFrame1,width=160, height=60,
          image=self.img1).grid(row=0,column=0,padx=4,pady=4)

        self.img2 = PhotoImage(file=r"ATM_Icon\\two.png")
        self.btn2 = Button(TopFrame1,width=160, height=60,
          image=self.img2).grid(row=0,column=1,padx=4,pady=4)

        self.img3 = PhotoImage(file=r"ATM_Icon\\three.png")
        self.btn3 = Button(TopFrame1,width=160, height=60,
          image=self.img3).grid(row=0,column=2,padx=4,pady=4)

        self.imgCE = PhotoImage(file=r"ATM_Icon\\cancel.png")
        self.btnCancel = Button(TopFrame1,width=160, height=60,
          image=self.imgCE).grid(row=0,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************
        #**************************Pin number buttons*****************************

        self.img4 = PhotoImage(file=r"ATM_Icon\\four.png")
        self.btn4 = Button(TopFrame1,width=160, height=60,
          image=self.img4).grid(row=1,column=0,padx=4,pady=4)

        self.img5 = PhotoImage(file=r"ATM_Icon\\five.png")
        self.btn5 = Button(TopFrame1,width=160, height=60,
          image=self.img5).grid(row=1,column=1,padx=4,pady=4)

        self.img6 = PhotoImage(file=r"ATM_Icon\\six.png")
        self.btn6 = Button(TopFrame1,width=160, height=60,
          image=self.img6).grid(row=1,column=2,padx=4,pady=4)

        self.imgCL = PhotoImage(file=r"ATM_Icon\\clear.png")
        self.btnClear = Button(TopFrame1,width=160, height=60,
          image=self.imgCL).grid(row=1,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************
        #**************************Pin number buttons*****************************

        self.img7 = PhotoImage(file=r"ATM_Icon\\seven.png")
        self.btn7 = Button(TopFrame1,width=160, height=60,
          image=self.img7).grid(row=2,column=0,padx=4,pady=4)

        self.img8 = PhotoImage(file=r"ATM_Icon\\eight.png")
        self.btn8 = Button(TopFrame1,width=160, height=60,
          image=self.img8).grid(row=2,column=1,padx=4,pady=4)

        self.img9 = PhotoImage(file=r"ATM_Icon\\nine.png")
        self.btn9 = Button(TopFrame1,width=160, height=60,
          image=self.img9).grid(row=2,column=2,padx=4,pady=4)

        self.img0 = PhotoImage(file=r"ATM_Icon\\zero.png")
        self.btn0 = Button(TopFrame1,width=160, height=60,
          image=self.img0).grid(row=3,column=1,padx=4,pady=4)

        self.imgEN = PhotoImage(file=r"ATM_Icon\\enter.png")
        self.btnEnter = Button(TopFrame1,width=160, height=60,
          image=self.imgEN).grid(row=2,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************
        #**************************Pin number buttons*****************************
        self.imgsp1 = PhotoImage(file=r"ATM_Icon\\empty.png")
        self.btnSp1 = Button(TopFrame1,width=160, height=60,
          image=self.imgsp1).grid(row=3,column=0,padx=4,pady=4)

        self.img0 = PhotoImage(file=r"ATM_Icon\\zero.png")
        self.btn0 = Button(TopFrame1,width=160, height=60,
          image=self.img0).grid(row=3,column=1,padx=4,pady=4)

        self.imgsp2 = PhotoImage(file=r"ATM_Icon\\empty.png")
        self.btnSp2 = Button(TopFrame1,width=160, height=60,
          image=self.imgsp2).grid(row=3,column=2,padx=4,pady=4)

        self.imgsp3 = PhotoImage(file=r"ATM_Icon\\empty.png")
        self.btnSp3 = Button(TopFrame1,width=160, height=60,
          image=self.imgsp3).grid(row=3,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************







        

        

        
        
        

if __name__ == "__main__":
    root = Tk()
    application = atm(root)
    root.mainloop()

