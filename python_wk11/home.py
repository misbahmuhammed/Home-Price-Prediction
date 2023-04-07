from functools import partial
from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('EDU-CART')
ws['bg'] = '#5d8a82'

f = ("Times bold", 14)

class Registration:
    def detailsForm(self,ws):
        ws.destroy()
        import registration

data = Registration()
window = partial(data.detailsForm,ws)



def returnForm():
    ws.destroy()
    import returnbook


Label(
    ws,
    text="Welcome To EduCart",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Borrowing",
    font=f,
    command=window
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Return",
    font=f,
    command=returnForm
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
