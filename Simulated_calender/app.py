from tkinter import * 

from tkcalender import * 

root=  Tk()
root.titel('Calender: ')
root.geometry('600x488')

cal = Calender(root, year=  2022 ,  mounth = 1 , days=7).pack(pady=0 )


root.mainloop()

