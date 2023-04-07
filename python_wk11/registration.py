from tkinter import *

def callback():
    book_id = bookid.get()

    book_name = bookname.get()
    book_name = str(book_name)

    borrow_name = borrowname.get()
    borrow_name = str(borrow_name)

    borrow_date = borroweddate.get()
    borrow_date = str(borrow_date)


    print(book_id ,"\n",  book_name,"\n",  borrow_name , "\n" , borroweddate)
    ls1=[book_id,book_name,borrow_name,borrow_date]
    file = open("data.txt", "a")
    file.write(str(ls1))

    file.close()
    print("USER :",borrow_name  , "has been regustered successfully" )

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))


Bookid_text = Label(root, text="Book Id", width=20, font=("bold", 10))
Bookid_text.place(x=130, y=130)

bookid =  StringVar()
Bookid_entry = Entry(textvariable= bookid)
Bookid_entry.place(x=240, y=130)

Bookname_text = Label(root, text="Book Name", width=20, font=("bold", 10))
Bookname_text.place(x=120, y=180)

bookname =  StringVar()

bookname_entry = Entry(textvariable=bookname)
bookname_entry.place(x=240, y=180)

Borrowed_date = Label(root, text="Date", width=20, font=("bold", 10))
Borrowed_date.place(x=143, y=245)

borroweddate =  StringVar()

borroweddate_entry = Entry(textvariable=borroweddate)
borroweddate_entry.place(x=240, y=245)

borrowperson_text = Label(root, text="Borrowed Person Name", width=20, font=("bold", 10))
borrowperson_text.place(x=85, y=280)

borrowname = StringVar()

Borrowperson_name = Entry(textvariable=borrowname)
Borrowperson_name.place(x=240, y=280)








save = Button(root, text='Submit', width=20, bg='brown', fg='white',command=callback)
save.place(x=180, y=380)
# it is use for display the registration form on the window
root.mainloop()

