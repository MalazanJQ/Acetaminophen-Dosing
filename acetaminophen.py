from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(lbs.get())
        weight = (value / 2.2)
        kgs.set(round(weight, 2))
        mindose.set(round((float(kgs.get()) * 10 / 160 * 5), 2))
        maxdose.set(round((float(kgs.get()) * 15 / 160 * 5), 2))
        dailydose.set(round((float(kgs.get()) * 75) / 160 * 5, 2))
    except ValueError:
        pass

root = Tk()
root.title("Weight-Based Acetaminophen Dosing")
rb = 'rosybrown1'
ttk.Style().configure(root, background=rb)
mainframe = ttk.Frame(root, padding="4 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

lbs = StringVar()
kgs = StringVar()
mindose = StringVar()
maxdose = StringVar()
dailydose = StringVar()

lbs_entry = ttk.Entry(mainframe, width=7, textvariable=lbs)
lbs_entry.grid(column=1, row=1, sticky=(W, E))
Label(mainframe, textvariable=kgs, bg=rb).grid(column=3, row=1, sticky=(W, E))
Label(mainframe, textvariable=mindose, bg=rb).grid(column=1, row=2, sticky=E)
Label(mainframe, textvariable=maxdose, bg=rb).grid(column=3, row=2, sticky=(W,E))
Label(mainframe, textvariable=dailydose, bg=rb).grid(column=2, row=3, sticky=(W, E))
Button(mainframe, text="Calculate", command=calculate,
       bg='rosybrown3').grid(column=4, row=3, sticky=W)

Label(mainframe, text=" lbs = ", bg=rb).grid(column=2, row=1, sticky=(W, E))
Label(mainframe, text="kgs", bg=rb).grid(column=4, row=1, sticky=W)
Label(mainframe, text="to", bg=rb).grid(column=2, row=2)
Label(mainframe, text="mls every 4 to 6 hrs", bg=rb).grid(column=4, row=2, sticky=W)
Label(mainframe, text="Max", bg=rb).grid(column=1, row=3, sticky=E)
Label(mainframe, text="mLs daily", bg=rb).grid(column=3, row=3, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
lbs_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

"""Dose Citation:
    Gold Standard, Inc. Acetaminophen. Clinical Pharmacology [database online].
    Available at: http://www.clinicalpharmacology.com. Accessed: July, 9, 2020."""