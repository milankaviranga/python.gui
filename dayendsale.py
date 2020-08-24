from tkinter import *

root = Tk()
root.geometry("1360x768+0+0")
root.title('Find Day Sale-by Milan Kaviranga')
root.configure(background='dark gray')

titlabel = Label(root, text='FIND DAY END SALE', foreground='blue', background='yellow')
titlabel.configure(font=('Calibri (Body)',30,'bold'))
titlabel.place(x=480, y=12)




# Software all Functions

ds = StringVar()
ch = StringVar()
cr = StringVar()
te = StringVar()
pca = StringVar()
des = StringVar()
ot = StringVar()
tot = StringVar()
totlabels = StringVar()
othercashd = StringVar()

def fin():
    dsf = ds.get()
    chf = ch.get()
    crf = cr.get()
    tef = te.get()
    pcaf = pca.get()
    desf = des.get()
    otf = ot.get()
    otcf = othercashd.get()


    chft = str(eval(chf))
    crt = str(eval(crf))


    allt = (int(chft)+
                int(crt)+int(tef)+

            int(pcaf)+
                int(desf)+int(otf))

    discou = int(dsf)+int(otcf) - allt


    tot.set('RS.'+str(discou))






def clear():
    dsf = ds.set("")
    chf = ch.set("")
    crf = cr.set("")
    tef = te.set("")
    pcaf = pca.set("")
    desf = des.set("")
    otf = ot.set("")
    otcf = othercashd.set("")
    tot.set("")

def ext():
    root.destroy()



#daysale information

daysale = Label(root, text='Day Sale')
daysale.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
daysale.place(x=50, y=150)

daysaleent = Entry(root, width=12, textvar=ds)
daysaleent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
daysaleent.place(x=150, y=155)

#check detalis

check = Label(root, text='Check')
check.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
check.place(x=50, y=200)

checkent = Entry(root, width=12, textvar=ch)
checkent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
checkent.place(x=150, y=200)


# Credit details

credit = Label(root, text='Credit')
credit.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
credit.place(x=50, y=250)

creditent = Entry(root, width=12, textvar=cr)
creditent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
creditent.place(x=150, y=250)

# tea details

tea = Label(root, text='Tea')
tea.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
tea.place(x=50, y=300)

teaent = Entry(root, width=12, textvar=te)
teaent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
teaent.place(x=150, y=300)

# P cash

pcash = Label(root, text='P Cash')
pcash.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
pcash.place(x=500, y=150)

pcashent = Entry(root, width=12, textvar=pca)
pcashent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
pcashent.place(x=590, y=154)

# Desal cash

desal = Label(root, text='Desal')
desal.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
desal.place(x=500, y=200)

desalent = Entry(root, width=12, textvar=des)
desalent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
desalent.place(x=590, y=200)

# Other

other = Label(root, text='Other')
other.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='dark red')
other.place(x=500, y=250)

otherent = Entry(root, width=12, textvar=ot)
otherent.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
otherent.place(x=590, y=250)


# All details

totlabel = Label(root, text="Other C")
totlabel.configure(font=('Calibri (Body)',14,'bold'),background='dark gray', foreground='purple')
totlabel.place(x=500, y=300)

othercash = Entry(root, text='Total', textvar=othercashd)
othercash.configure(font=('Calibri (Body)',12,'bold'),width=30, relief='sunken', borderwidth=2, background='skyblue')
othercash.place(x=590, y=300)


# Button

button = Button(root, text='FIND', command=fin, width=15, height=2)
button.configure(font=('Courier New',15,'bold'),borderwidth=3,background='pink', foreground='black')
button.place(x=150, y=400)

button1 = Button(root, text='CLEAR', command=clear, width=15, height=2)
button1.configure(font=('Courier New',15,'bold'),borderwidth=3,background='pink', foreground='black')
button1.place(x=420, y=400)

button1 = Button(root, text='EXIT', command=ext, width=15, height=2)
button1.configure(font=('Courier New',15,'bold'),borderwidth=3,background='pink', foreground='black')
button1.place(x=675, y=400)

# final result

totlabelsa = Label(root, textvar=tot)
totlabelsa.configure(background='white', width=27, height=3, font=('Courier New',20,'bold'))
totlabelsa.place(x=420, y=500)




#-------------------------------------------------------------------------

f1 = Frame(root).pack()

melabel = Label(root, text="CALCULATOR", bg='White', font=("Times", 30, 'bold'))
melabel.place(x=1040, y=12)


textin = StringVar()
operator = ""


def clickbut(numbers):
    global operator
    operator=operator + str(numbers)
    textin.set(operator)

def clrbut():
    global operator
    operator=""
    textin.set("")

def equlbut():
    global operator
    setup=str(eval(operator))

    textin.set(setup)
    operator = ""


metext = Entry(f1, font=("Courier New", 12, 'bold'), textvar=textin, width=32, bd=5, bg='powder blue')
metext.place(x=1015, y=75)

but1 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=1010, y=110)

but2 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=1010, y=180)

but3 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=1010, y=250)

but4 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=1075, y=110)

but5 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=1075, y=180)

but6 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=1075, y=250)

but7 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=1140, y=110)

but8 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=1140, y=180)

but9 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=1140, y=250)

but0 = Button(f1, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=1010, y=320)

butdot = Button(f1, padx=47, pady=14, bd=4, bg='white', command=lambda: clickbut("."), text=".",
                font=("Courier New", 16, 'bold'))
butdot.place(x=1075, y=320)

butpl = Button(f1, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=1205, y=110)

butsub = Button(f1, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=1205, y=180)

butml = Button(f1, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
               font=("Courier New", 16, 'bold'))
butml.place(x=1205, y=250)

butdiv = Button(f1, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                font=("Courier New", 16, 'bold'))
butdiv.place(x=1205, y=320)

butclear = Button(f1, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut, font=("Courier New", 16, 'bold'))
butclear.place(x=1270, y=110)

butequal = Button(f1, padx=151, pady=14, bd=4, bg='white', command=equlbut, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=1010, y=390)
#----------------------------------------------------------------------


root.mainloop()
