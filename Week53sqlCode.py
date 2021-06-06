from tkinter import *
import Week53sqlModule as wsm

window = Tk()

main_frm = LabelFrame(window)

name_lbl = Label(main_frm,text = 'Enter your name ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
name_ent = Entry(main_frm)
birthPlace_lbl = Label(main_frm,text = 'Where is your birth place ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
birthPlace_ent = Entry(main_frm)
age_lbl = Label(main_frm,text = 'Enter your age ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
age_ent = Entry(main_frm)
submit_btn = Button(main_frm,text = 'Submit',width = 20,height = 3,command = lambda: wsm.write_fun(name_ent.get(),birthPlace_ent.get(),age_ent.get())).grid(row = 3, column = 0, padx = 10, pady = 10)

main_frm.grid(row = 0, column = 0, padx = 10, pady = 10)
name_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
birthPlace_ent.grid(row = 1, column = 1, padx = 10, pady = 10)
age_ent.grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()