from tkinter import *
import pymysql

class main():
    def getval(self):
        self.gender = "Male" if var.get() == 0 else "Female"
        self.angular = "Yes" if var1.get() == 1 else "No"
        self.react = "Yes" if var2.get() == 1 else "No"

    def submit(self):
        self.name = a1.get()
        self.email = b1.get()
        self.password = e1.get()
        window.destroy()
        db = pymysql.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE PERSON(
                     NAME  CHAR(20) NOT NULL,
                     EMAIL CHAR(30) NOT NULL,
                     PASSWORD CHAR(30) NOT NULL,
                     GENDER CHAR(5) NOT NULL,
                     ANGULAR CHAR(5) NOT NULL,
                     REACT CHAR(5) NOT NULL)""")

        cursor.execute("""INSERT INTO PERSON
                    (NAME, EMAIL, PASSWORD, GENDER, ANGULAR, REACT)
                    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(self.name, self.email, self.password, self.gender, self.angular, self.react))
        db.commit()
        db.close()


window = Tk()
window.title("Registration")
window.geometry('325x200')
var = IntVar()
var1 = IntVar()
var2 = IntVar()
m = main()

frame1 = Frame(window)
a = Label(frame1 ,text = "Full Name:", width = 15, anchor = 'w')
a1 = Entry(frame1, bd=1)

frame2 = Frame(window)
b = Label(frame2 ,text = "Email:", width = 15, anchor = 'w')
b1 = Entry(frame2, bd=1)

frame6 = Frame(window)
e = Label(frame6 ,text = "Password:", width = 15, anchor = 'w')
e1 = Entry(frame6, bd=1, show="*")

frame3 = Frame(window)
c = Label(frame3, text= "Gender:", width = 16, anchor = 'w')
c1 = Radiobutton(frame3, text = "Male",variable = var,value = 0,command = m.getval)
c2 = Radiobutton(frame3, text = "Female",variable = var,value = 1,command = m.getval)

frame4 = Frame(window)
d = Label(frame4, text= "Technology:", width = 15, anchor = 'w')
d1 = Checkbutton(frame4, text = "Angular", variable = var1, onvalue = 1, offvalue = 0, command = m.getval)
d2 = Checkbutton(frame4, text = "React", variable = var2, onvalue = 1, offvalue = 0, command = m.getval)

frame5 = Frame(window)
button = Button(frame5, text = "Submit", command = m.submit)

frame1.pack()
a.pack(side = LEFT)
a1.pack(side = RIGHT, pady=5)
name = a1.get()

frame2.pack()
b.pack(side = LEFT)
b1.pack(side = RIGHT, pady=5)

frame6.pack()
e.pack(side = LEFT)
e1.pack(side = RIGHT, pady=5)

frame3.pack()
c.pack(side = LEFT)
c1.pack(side = LEFT)
c2.pack(side = RIGHT)

frame4.pack()
d.pack(side = LEFT)
d1.pack(side = LEFT)
d2.pack(side = RIGHT)

frame5.pack()
button.pack(side=BOTTOM)

window.mainloop()