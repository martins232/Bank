from email.mime import image
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
        self.root.resizable(0,0)
        #**************************frames******************************
        MainFrame = Frame(self.root, bd=20, width=784, height=700,
                          relief=SUNKEN)
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
        #***********************functions*****************************
        def enter_pin():
          pinNo = self.txtReceipt.get("1.0","end-1c")
          if ((pinNo==str(2222))or (pinNo==str(1234))):
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END, "\t\tATM" + "\n\n")
            self.txtReceipt.insert(END, "LOAN\t\t\tWITHDRAW CASH" + " \n\n\n\n")
            self.txtReceipt.insert(END, "DEPOSIT\t\t\tACCOUNT BALANCE" + " \n\n\n\n")
            self.txtReceipt.insert(END, "STATEMENT\t\t\tCLOSE ACCOUNT" + " \n\n\n\n")

            #**************************Enable_Left_widgets*****************************
            self.btnArrow_Left = Button(TopFrame2Left,width=160, height=60,
              image=self.img_arrow_Left, state=NORMAL).grid(row=0,column=0,padx=2,pady=1)

            self.btnArrow_Left1 = Button(TopFrame2Left,width=160, height=60,
              image=self.img_arrow_Left, state=NORMAL).grid(row=1,column=0,padx=2,pady=1)

            self.btnArrow_Left2 = Button(TopFrame2Left,width=160, height=60,
              image=self.img_arrow_Left, state=NORMAL).grid(row=2,column=0,padx=2,pady=1)

            self.btnArrow_Left3 = Button(TopFrame2Left,width=160, height=60,
              image=self.img_arrow_Left, state=NORMAL).grid(row=3,column=0,padx=2,pady=1)

            #**************************Enable_Right_widgets*****************************
            self.btnArrow_Right = Button(TopFrame2Right,width=160, height=60,
              image=self.img_arrow_right, state=NORMAL).grid(row=0,column=0,padx=2,pady=1)

            self.btnArrow_Right1 = Button(TopFrame2Right,width=160, height=60,
              image=self.img_arrow_right, state=NORMAL).grid(row=1,column=0,padx=2,pady=1)

            self.btnArrow_Right2 = Button(TopFrame2Right,width=160, height=60,
              image=self.img_arrow_right, state=NORMAL).grid(row=2,column=0,padx=2,pady=1)

            self.btnArrow_Right3 = Button(TopFrame2Right,width=160, height=60,
              image=self.img_arrow_right, state=NORMAL).grid(row=3,column=0,padx=2,pady=1)
          else:
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END, "\t\tInvalid Pin" + "\n\n")
        def clear():
          self.txtReceipt.delete("1.0",END)
            #**************************Left_widgets*****************************
          self.btnArrow_Left = Button(TopFrame2Left,width=160, height=60,
            image=self.img_arrow_Left, state=DISABLED).grid(row=0,column=0,padx=2,pady=1)

          self.btnArrow_Left1 = Button(TopFrame2Left,width=160, height=60,
            image=self.img_arrow_Left, state=DISABLED).grid(row=1,column=0,padx=2,pady=1)

          self.btnArrow_Left2 = Button(TopFrame2Left,width=160, height=60,
            image=self.img_arrow_Left, state=DISABLED).grid(row=2,column=0,padx=2,pady=1)

          self.btnArrow_Left3 = Button(TopFrame2Left,width=160, height=60,
            image=self.img_arrow_Left, state=DISABLED).grid(row=3,column=0,padx=2,pady=1)

          #**************************Right_widgets*****************************
          self.btnArrow_Right = Button(TopFrame2Right,width=160, height=60,
            image=self.img_arrow_right, state=DISABLED).grid(row=0,column=0,padx=2,pady=1)

          self.btnArrow_Right1 = Button(TopFrame2Right,width=160, height=60,
            image=self.img_arrow_right, state=DISABLED).grid(row=1,column=0,padx=2,pady=1)

          self.btnArrow_Right2 = Button(TopFrame2Right,width=160, height=60,
            image=self.img_arrow_right, state=DISABLED).grid(row=2,column=0,padx=2,pady=1)

          self.btnArrow_Right3 = Button(TopFrame2Right,width=160, height=60,
            image=self.img_arrow_right, state=DISABLED).grid(row=3,column=0,padx=2,pady=1)
        def insert0():
          value0 = 0
          self.txtReceipt.insert(END, value0)
        def insert1():
          value1 = 1
          self.txtReceipt.insert(END, value1)
        def insert2():
          value2 = 2
          self.txtReceipt.insert(END, value2)
        def insert3():
          value3 = 3
          self.txtReceipt.insert(END, value3)
        def insert4():
          value4 = 4
          self.txtReceipt.insert(END, value4)
        def insert5():
          value5 = 5
          self.txtReceipt.insert(END, value5)
        def insert6():
          value6 = 6
          self.txtReceipt.insert(END, value6)
        def insert7():
          value7 = 7
          self.txtReceipt.insert(END, value7)
        def insert8():
          value8 = 8
          self.txtReceipt.insert(END, value8)
        def insert9():
          value9 = 9
          self.txtReceipt.insert(END, value9)
        def cancel():
          cancel= tkinter.messagebox.askyesno("KUDA", "Confirm if you want to cancel")
          if cancel>0:
            self.root.destroy()
            return
        # *************************functions end**********************8
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
          image=self.img1,command=insert1).grid(row=0,column=0,padx=4,pady=4)

        self.img2 = PhotoImage(file=r"ATM_Icon\\two.png")
        self.btn2 = Button(TopFrame1,width=160, height=60,
          image=self.img2, command=insert2).grid(row=0,column=1,padx=4,pady=4)

        self.img3 = PhotoImage(file=r"ATM_Icon\\three.png")
        self.btn3 = Button(TopFrame1,width=160, height=60,
          image=self.img3, command=insert3).grid(row=0,column=2,padx=4,pady=4)

        self.imgCE = PhotoImage(file=r"ATM_Icon\\cancel.png")
        self.btnCancel = Button(TopFrame1,width=160, height=60,
          image=self.imgCE,command=cancel).grid(row=0,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************
        #**************************Pin number buttons*****************************

        self.img4 = PhotoImage(file=r"ATM_Icon\\four.png")
        self.btn4 = Button(TopFrame1,width=160, height=60,
          image=self.img4, command=insert4).grid(row=1,column=0,padx=4,pady=4)

        self.img5 = PhotoImage(file=r"ATM_Icon\\five.png")
        self.btn5 = Button(TopFrame1,width=160, height=60,
          image=self.img5,command=insert5).grid(row=1,column=1,padx=4,pady=4)

        self.img6 = PhotoImage(file=r"ATM_Icon\\six.png")
        self.btn6 = Button(TopFrame1,width=160, height=60,
          image=self.img6, command=insert6).grid(row=1,column=2,padx=4,pady=4)

        self.imgCL = PhotoImage(file=r"ATM_Icon\\clear.png")
        self.btnClear = Button(TopFrame1,width=160, height=60,
          image=self.imgCL, command=clear).grid(row=1,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************
        #**************************Pin number buttons*****************************

        self.img7 = PhotoImage(file=r"ATM_Icon\\seven.png")
        self.btn7 = Button(TopFrame1,width=160, height=60,
          image=self.img7, command=insert7).grid(row=2,column=0,padx=4,pady=4)

        self.img8 = PhotoImage(file=r"ATM_Icon\\eight.png")
        self.btn8 = Button(TopFrame1,width=160, height=60,
          image=self.img8, command=insert8).grid(row=2,column=1,padx=4,pady=4)

        self.img9 = PhotoImage(file=r"ATM_Icon\\nine.png")
        self.btn9 = Button(TopFrame1,width=160, height=60,
          image=self.img9, command=insert9).grid(row=2,column=2,padx=4,pady=4)

        self.img0 = PhotoImage(file=r"ATM_Icon\\zero.png")
        self.btn0 = Button(TopFrame1,width=160, height=60,
          image=self.img0).grid(row=3,column=1,padx=4,pady=4)

        self.imgEN = PhotoImage(file=r"ATM_Icon\\enter.png")
        self.btnEnter = Button(TopFrame1,width=160, height=60,
          image=self.imgEN,command=enter_pin).grid(row=2,column=3,padx=4,pady=4)
        #**************************Pin number buttons*****************************
        #**************************Pin number buttons*****************************
        self.imgsp1 = PhotoImage(file=r"ATM_Icon\\empty.png")
        self.btnSp1 = Button(TopFrame1,width=160, height=60,
          image=self.imgsp1).grid(row=3,column=0,padx=4,pady=4)

        self.img0 = PhotoImage(file=r"ATM_Icon\\zero.png")
        self.btn0 = Button(TopFrame1,width=160, height=60,
          image=self.img0, command=insert0).grid(row=3,column=1,padx=4,pady=4)

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

