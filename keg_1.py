from Tkinter import *
pro = Tk (className = ' Data Diri')
pro.geometry('350x200')

judul = Label (pro, text="Data Diri", font=('Arial 27 bold'))
judul.grid(row=0, column=0)

data1 = Label (pro, text="Nama")
data1.grid(row=1, column=0, sticky='w')
data2 = Label (pro, text="Karina Muslimah")
data2.grid(row=1, column=1, sticky='w')
data3 = Label (pro, text="NIM")
data3.grid(row=2, column=0, sticky='w')
data4 = Label (pro, text="L200180138")
data4.grid(row=2, column=1, sticky='w')
data5 = Label (pro, text="Buku Favorit")
data5.grid(row=3, column=0, sticky='w')
data6 = Label (pro, text="Emmmm.. Entahlah")
data6.grid(row=3, column=1, sticky='w')
data7 = Label (pro, text="Idola di kalangan sahabat")
data7.grid(row=4, column=0, sticky='w')
data8 = Label (pro, text="Abu Bakar Ash Shidiq")
data8.grid(row=4, column=1, sticky='w')
data9 = Label (pro, text="Abu Bakar Ash Shidiq")
data9.grid(row=4, column=0, sticky='w')


tombol = Button (pro, text="TUTUP", command=pro.destroy)
tombol.grid(row=5, column=1, sticky='w')

pro.mainloop()
