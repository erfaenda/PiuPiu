from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

btn1 = Button(top_frame, text='Button_1', fg='green')
btn2 = Button(top_frame, text='Button_2', fg='green')
btn3 = Button(top_frame, text='Button_3', fg='green')
btn4 = Button(bottom_frame, text='Button_4', fg='green')

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack()

root.mainloop()
