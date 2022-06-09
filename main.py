from tkinter import *

gui = Tk()

c1 = Checkbutton(gui, text = "Python", height = 2, width = 10)
c2 = Checkbutton(gui, text = "Java", height = 2, width = 10)
c3 = Checkbutton(gui, text = "PHP", height = 2, width = 10)

c1.pack()
c2.pack()
c3.pack()

gui.mainloop()
